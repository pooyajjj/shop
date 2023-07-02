from django.http import JsonResponse
from accounts.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

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

        return JsonResponse(status=200, data=data, safe=False)

    except:
        return JsonResponse(status=400, data={"inform":"user can not be created"})
