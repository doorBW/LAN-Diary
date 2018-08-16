from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('mydiary/', views.mydiary),
    path('setting/', views.setting),
    path('writediary/', views.write_diary),
    path('pickdiary/', views.pick_diary),
    path('groupdiary/<str:group>', views.group_diary, name="groupdiary"),
    path('makegroup/', views.make_group),
    path('makegroup/making', views.making_group),
    path('search/', views.search_group),
    path('invite/check/<str:token>', views.invite_check),
    path('invite/join/group', views.join_group),
    path('calendardiary', views.calendar_diary),
    path('test/404page', views.test_404page),
    path('test/errorpage', views.test_errorpage),
    path('test/unloginpage', views.test_unloginpage)
    # path('my_diary/', views.ViewMydiary.as_view(), name='ViewMydiary'),
    # path('write_diary/', views.write_diary, name='WriteDiary'),
    # path('edit_diary/<int:id>/', views.edit_diary, name='EditDiary'),
]
