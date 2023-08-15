from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ["email" , "username" , "age" , "gender" , "weight" , "height" , "weight_goal"]
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ["email" , "username" , "age" , "gender" , "weight" , "height" , "weight_goal"]