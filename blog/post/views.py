from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request,'base.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'blogcreatepage.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')