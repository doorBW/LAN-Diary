from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('mydiary/', views.mydiary),
    path('setting/', views.setting),
    path('writediary/', views.write_diary),
    path('pickdiary/', views.pick_diary),
    path('pick', views.pick, name='pick'),
    path('remove', views.remove),
    path('comment_delete', views.comment_delete),
    path('groupdiary/<str:group>', views.group_diary),
    path('makegroup/', views.make_group),
    path('search/', views.search_group),
    path('mydiary/select/',views.mydiary_select),
    path('mydiary_delete',views.mydiary_delete),
    # path('my_diary/', views.ViewMydiary.as_view(), name='ViewMydiary'),
    # path('write_diary/', views.write_diary, name='WriteDiary'),
    # path('edit_diary/<int:id>/', views.edit_diary, name='EditDiary'),
]
