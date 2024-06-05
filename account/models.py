# from typing import Any
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.crypto import get_random_string
# from django.contrib.auth.base_user import BaseUserManager
# from phonenumber_field.modelfields import PhoneNumberField
# class UserManager(BaseUserManager):
#     def _create_user(self, email, phome_number, password, **extra):
#         if not email:
#             raise ValueError('Email - поле обязательное')
#         if not phome_number:
#             raise ValueError('Phone number is required')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_user(self, email, password, **extra):
#         user = self._create_user(email, password, **extra)
#         user.create_activation_code() 
#         user.save()
#         return user 
    
#     def create_superuser(self, email, password, **extra):
#         extra.setdefault('is_active', True)
#         extra.setdefault('is_staff', True)
#         extra.setdefault('is_superuser', True)
#         user = self._create_user(email, password, **extra)
#         return user
    

# class User(AbstractUser):
#     username = None 
#     email = models.EmailField(unique=True)
#     phome_number = PhoneNumberField(unique=True, null=False, blank=False)
#     is_active = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=10, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def create_activation_code(self):
#         code = get_random_string(length=10, allowed_chars='0123456789')
#         self.activation_code = code

# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def _create_user(self, email, password, phone_number, **extra):
        if not email and not phone_number:
            raise ValueError('Email или номер телефона должны быть указаны')
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, phone_number=None, **extra):
        user = self._create_user(email, password, phone_number, **extra)
        user.create_activation_code()
        user.save()
        return user

    def create_superuser(self, email, password, phone_number=None, **extra):
        extra.setdefault('is_active', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        user = self._create_user(email, password, phone_number, **extra)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='0123456789')
        self.activation_code = code
