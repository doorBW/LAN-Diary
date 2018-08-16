from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('mydiary/', views.mydiary, name= 'mydiary'),
    path('setting/', views.setting),
    path('writediary/', views.write_diary, name= 'writediary'),
    path('pickdiary/', views.pick_diary),
    path('groupdiary/<str:group>', views.group_diary),
    path('makegroup/', views.make_group),
    path('search/', views.search_group),
    #path('writediary/writing', views.writing),
    path('<int:pk>/editdiary',views.edit_diary, name = 'editdiary'),
    # path('my_diary/', views.ViewMydiary.as_view(), name='ViewMydiary'),
    # path('write_diary/', views.write_diary, name='WriteDiary'),
    # path('edit_diary/<int:id>/', views.edit_diary, name='EditDiary'),
]
