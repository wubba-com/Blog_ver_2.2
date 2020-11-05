from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from django.urls import reverse_lazy

from .models import Post, Tags
from .forms import TagForm, PostForm


class BlogView(ListView):
    """Вывод всех статей"""
    model = Post
    queryset = Post.objects.all()
    template_name = 'post/posts_list.html'


class PostDetailView(DetailView):
    """Полная информаци статьи"""
    model = Post
    template_name = 'post/post_detail.html'
    slug_field = 'url'


class TagsListView(ListView):
    """Вывод всех тегов"""
    model = Tags
    template_name = 'post/tags_list.html'


class TagDetailView(DetailView):
    """Вывод статей по тегу"""
    model = Tags
    template_name = 'post/tag_detail.html'
    slug_field = 'url_tags'


class TagCreateView(CreateView):
    model = Tags
    form_class = TagForm
    template_name = 'post/tag_create.html'


class CreatePostView(CreateView):
    """Создание статьи пользователем"""
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_form.html'
