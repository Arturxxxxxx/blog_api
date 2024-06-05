# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth import get_user_model 
# from drf_yasg.utils import swagger_auto_schema

# from .serializers import RegisterSerializer

# User = get_user_model()

# class RegisterView(APIView):
#     @swagger_auto_schema(request_body=RegisterSerializer())
#     def post(self, request):
#         data = request.data
#         serializer = RegisterSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response('Вы успешно зарегистрировались!', 201)

# class ActivationView(APIView):
#     def get(self, request, email, activation_code):
#         user = User.objects.filter(email=email, activation_code=activation_code).first()
#         if not user:
#             return Response('Пользователь не найден', 404)
#         user.activation_code = ''
#         user.is_active = True
#         user.save()
#         return Response('Вы успешно активировали акаунт', 200)
# # views.py
# from rest_framework import generics
# from .serializers import UserRegistrationSerializer
# # from rest_framework.response import Response
# from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserRegistrationSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "User registered successfully"}, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model 
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Вы успешно зарегистрировались!', 201)


# class RegisterView(APIView):
#     @swagger_auto_schema(request_body=RegisterSerializer)
#     def post(self, request):
#         data = request.data
#         serializer = RegisterSerializer(data=data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "Вы успешно зарегистрировались!"}, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не найден', 404)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Вы успешно активировали аккаунт', 200)




