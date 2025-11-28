from msilib.schema import ListView

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Post


def index(request):
    return HttpResponse("Django работает!")

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
