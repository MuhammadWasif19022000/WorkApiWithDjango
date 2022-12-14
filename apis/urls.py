from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    path('student-view/<str:pk>/',views.studentview,name="studentview"),
    path('add-student',views.studentadd,name="studentadd"),
    path('update-student/<str:pk>/', views.studentupdate, name="studentupdate"),
    path('delete-student/<str:pk>/', views.studentdelete, name="studentdelete")
]
