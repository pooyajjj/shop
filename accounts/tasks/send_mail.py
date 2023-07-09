from django.core.mail import send_mail as send
from shop.settings import DEFAULT_FROM_EMAIL
from celery import shared_task

@shared_task
def send_mail(reciver, subject, message):
    send(
        subject=subject,
        message=message,
        from_email = DEFAULT_FROM_EMAIL,
        to_email = reciver
    )