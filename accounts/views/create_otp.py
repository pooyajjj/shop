from django.http import JsonResponse
from accounts.models import OTP,  CustomUser
from django.views.decorators.http import require_http_methods
from random import randrange
from accounts.tasks import send_mail

@require_http_methods(['GET'])
def create_otp(request ,id):
    code = OTP.objects.create(code = randrange(10000, 99999))
    user = CustomUser.objects.get(id = id)
    user.otp = code
    user.save()
    subject = 'active account with otp'
    message = f'here is your activation code ====> {user.code}'
    send_mail(reciver=user.email, subject=subject ,message=message)
    print(user.username, user.otp.code)
    return JsonResponse(data={"message":"hi"})