from . import views
from django.urls import path

urlpatterns =[
    path('',views.Json_formate,name='json_formate'),
    path('project/',views.json_project,name='json_project'),
    path('student/',views.StudentApiWithoutId,name ="StudentWithoutId"),
    path('student/<str:pk>/',views.StudentApiWithId,name="StudentWithId"),
]