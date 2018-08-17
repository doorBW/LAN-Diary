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
    path('pickdiary_comment_delete', views.pickdiary_comment_delete),
    path('calendardiary_comment_delete', views.calendardiary_comment_delete),
    path('mydiary_delete',views.mydiary_delete),
    path('calendardiary/', views.calendar_diary, name='calendardiary'),
    path('calendardiary_delete',views.calendardiary_delete),
    path('comment_delete_2', views.comment_delete_2),
    # path('my_diary/', views.ViewMydiary.as_view(), name='ViewMydiary'),
    # path('write_diary/', views.write_diary, name='WriteDiary'),
    # path('edit_diary/<int:id>/', views.edit_diary, name='EditDiary'),
    path('<int:pk>/editdiary',views.edit_diary, name = 'editdiary'),
]
