from django.shortcuts import render
from .models import Users
# Create your views here.


def index(request):
    users = Users.objects.all()
    return render(request, 'mainPage/index.html', {
        'flag': True,
        'users': users
    })


def user_detail(request, user):
    user = Users.objects.get(slug=user)
    return render(request, 'mainPage/user_detail.html', {
        'user': user
    })
