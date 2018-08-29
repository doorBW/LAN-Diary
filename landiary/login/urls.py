from django.urls import path
from . import views
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.login),
    path('loging', views.loging),
    path('logout', views.logout),
    path('404page/', views.test_404page),
    path('errorpage/', views.test_errorpage),
    path('unloginpage/', views.test_unloginpage),
]

#urlpatterns += static(
#    settings.MEDIA_URL,
#    document_root=settings.MEDIA_ROOT
#)

