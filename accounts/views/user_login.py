from django.http import JsonResponse
from accounts.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(['POST'])
def user_login(requset):
    try:
        username = requset.POST['username'].lower()
        password = requset.POST['password']

        print(username, password, '444444444444444444444444444444444')

    except:
        return JsonResponse(status=400, data={"message":"username or password can not be empty"})

    try:
        user = authenticate(requset, username=username, password=password)
        print(user, '0000000000000000000000000000000000')
    except:
        return JsonResponse(status=400, data={"message":"username or password is wrong"})
    
    # if user is not None:
    login(requset, user)
    return JsonResponse(status=200, data={"message":"login successful"})

    # else:
    #     return JsonResponse(status=400, data={"message":"login faild please try again"})