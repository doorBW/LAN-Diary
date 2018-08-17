from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('mydiary/', views.mydiary, name= 'mydiary'),
    path('setting/', views.setting),
    path('writediary/', views.write_diary, name= 'writediary'),
    path('pickdiary/', views.pick_diary),
    path('groupdiary/<str:group>', views.group_diary, name="groupdiary"),
    path('makegroup/', views.make_group),
    path('makegroup/making', views.making_group),
    path('search/', views.search_group),
    path('invite/check/<str:token>', views.invite_check),
    path('invite/join/group', views.join_group),
    path('pick', views.pick, name='pick'),
    path('remove', views.remove),
    path('comment_delete', views.comment_delete),
    path('mydiary_delete',views.mydiary_delete),
    path('<int:pk>/editdiary',views.edit_diary, name = 'editdiary'),
]
