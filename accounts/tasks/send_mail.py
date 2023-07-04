from django.core.mail import send_mail as send
from shop.settings import DEFAULT_FROM_EMAIL
from celery import shared_task

@shared_task
def send_mail(reciver, user):
    send(
        subject='wellcome user',
        message=f'hello { user }, wellcome to our site and we hope you have a great time in this site',
        from_email = DEFAULT_FROM_EMAIL,
        to_email = reciver
    )