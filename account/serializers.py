# from rest_framework import serializers
# from django.contrib.auth import get_user_model

# from .utils import send_activation_code

# User = get_user_model()

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=4, required=True, write_only=True)
#     password_confirm = serializers.CharField(min_length = 4, required=True, write_only=True)

#     class Meta:
#         model = User 
#         fields = 'email', 'password', 'password_confirm'

#     def validate(self, attrs):
#         p1 = attrs.get('password')
#         p2 = attrs.pop('password_confirm')

#         if p1 != p2:
#             raise serializers.ValidationError('Пароли не совпали!')
#         return attrs
    
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         send_activation_code(user.email, user.activation_code)
#         return user 
from rest_framework import serializers
from django.contrib.auth import get_user_model


from .utils import send_activation_code, send_activation_sms

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=4, required=True, write_only=True)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password', 'password_confirm')

    def validate(self, attrs):
        email = attrs.get('email')
        phone_number = attrs.get('phone_number')
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')

        if not email and not phone_number:
            raise serializers.ValidationError('Необходимо указать либо email, либо номер телефона.')
        
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпали!')
        
        return attrs
    


    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        phone_number = validated_data.get('phone_number')

        user = User.objects.create_user(email=email, password=password, phone_number=phone_number)
        user.create_activation_code()
        user.save()

        if email:
            send_activation_code(user.email, user.activation_code)
        if phone_number:
            send_activation_sms(user.phone_number, user.activation_code)

        return user


