from django.urls import path,include
from project_app import views


urlpatterns = [

    path('',views.home,name='homepage'),
    path('about_us/<str:ids>/',views.about,name="ayush"),
    path('nav/',views.nav,name='piyush'),
    path('create_form/',views.create_form,name = 'project_form'),
    path('update_form/<str:ids>/',views.update_form,name='update_form'),
    path('delete_project/<str:ids>/',views.delete_form,name='delete_project'),
    
    
]
