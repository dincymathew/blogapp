from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registrations.html'
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('/')
