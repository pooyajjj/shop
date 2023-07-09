from django.http import JsonResponse
from accounts.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from accounts.tasks import send_mail

@csrf_exempt
@require_http_methods(['POST'])
def user_register(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        CustomUser.objects.create_user(username=username, email=email, password=password, phone=phone_number, is_special=False, is_active=False)

        data = {
            "username":username,
            "email":email,
            "phone_number":phone_number
        }
        message =f'hello dear {username} wellcome to our site i wish you have grate time'
        subject = 'wellcome mail'

        try:
            send_mail(reciver=email, message=message, subject=subject)
        except:
            print("can't send email")

        return JsonResponse(status=200, data=data, safe=False)

    except:
        return JsonResponse(status=400, data={"inform":"user can not be created, becase username or email or phone_number already used"})
