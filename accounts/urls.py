from .views import Home , SignUpView
from django.urls import path , include


urlpatterns = [
    
    path('' , Home.as_view() , name='home'),
    path('signup/' , SignUpView.as_view() , name='signup'),
    
    
]