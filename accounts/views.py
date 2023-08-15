from django.urls import reverse_lazy
from django.views.generic import TemplateView , CreateView

from .forms import CustomUserCreationForm

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"