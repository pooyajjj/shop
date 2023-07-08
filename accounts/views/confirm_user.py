from models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin

@LoginRequiredMixin
@require_http_methods(['GET'])
def confirm_user(request):
    user = CustomUser.objects.get(id=request.id)
