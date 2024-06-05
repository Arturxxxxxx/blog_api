from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_activation_code(email, activation_code):
    context = {
        'text_detail':'Спасибо за регистрацию!',
        'email':email,
        'domain':'http://localhost:8000',
        'activation_code':activation_code
    }
    msg_html = render_to_string('email.html', context)
    message = strip_tags(msg_html)

    send_mail(
        'Account Activation',
        message,
        'admin@admin.com',
        [email],
        html_message=msg_html,
        fail_silently=False
    )
    # utils.py
from twilio.rest import Client

def send_activation_sms(phone_number, activation_code):
    account_sid = 'your_account_sid'  # Замените на ваш Account SID
    auth_token = 'your_auth_token'    # Замените на ваш Auth Token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your activation code is {activation_code}',
        from_='+1234567890',  # Замените на ваш Twilio номер
        to=phone_number
    )
