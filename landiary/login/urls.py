from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('loging', views.loging),
    path('logout', views.logout),
    path('404page/', views.test_404page),
    path('errorpage/', views.test_errorpage),
    path('unloginpage/', views.test_unloginpage),
]
