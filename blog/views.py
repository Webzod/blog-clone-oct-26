from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'read.html'
    #context_object_name = 'post_list'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    #context_object_name = 'post_list'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content']

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post-update.html'
    fields = ['title', 'content']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post-list')

class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content' , 'author']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post-update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post-list')