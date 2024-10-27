from random import randint

from django.conf import settings
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def generate_otp():
    return randint(1000, 9999)


def send_otp_to_email(email, otp_type):
    otp = generate_otp()
    data = {'otp': otp}
    html_body = render_to_string('mail.html', data)
    message = EmailMultiAlternatives(subject='Подтверждение электронного адреса', to=[email])
    message.attach_alternative(html_body, 'text/html')
    message.send()
    cache.set(otp, email, settings.OTP_TIME, version=otp_type)
