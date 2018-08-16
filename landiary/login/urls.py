from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('loging', views.loging),
    path('logout', views.logout)
]
