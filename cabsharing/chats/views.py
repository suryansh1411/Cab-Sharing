from django.shortcuts import render
from django.views.generic import ListView, CreateView
from chats.models import Post
from chats.forms import PostForm
# Create your views here.

class PostCreateView(CreateView):
    model=Post
    form_class=PostForm

class PostListView(ListView):
    model=Post
    context_object_name='post_list'
