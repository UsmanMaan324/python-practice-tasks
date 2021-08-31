from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('<slug:user>', views.user_detail, name='user_detail')
]
