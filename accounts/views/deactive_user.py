from models import CustomUser
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def deactive_user(request):
    try:
        user = CustomUser.objects.get(pk=request.id)
    except:
        return JsonResponse(status=400, data={'message':"can't find the user"})

    if user is not None:
        user.is_active = False
        user.save()

    return JsonResponse(status=200, data={'message':'user deactived'})