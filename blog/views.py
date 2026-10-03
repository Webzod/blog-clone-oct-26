from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'read.html'
    #context_object_name = 'post_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    #context_object_name = 'post_list'

    