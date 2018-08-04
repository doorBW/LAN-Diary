from django.urls import path
from . import views


urlpatterns = [
    path('my_diary/', views.ViewMydiary.as_view(), name='ViewMydiary'),
    path('write_diary/', views.write_diary, name='WriteDiary'),
    path('edit_diary/<int:id>/', views.edit_diary, name='EditDiary'),
]
