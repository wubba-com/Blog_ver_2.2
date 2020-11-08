from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from django.urls import reverse

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


class TagUpdateView(View):
    def get(self, request, slug):
        tag = Tags.objects.get(url_tags__iexact=slug)
        bound_form = TagForm(instance=tag)
        context = {
            'form': bound_form,
            'tag': tag
        }
        return render(request, 'post/tag_update_form.html', context)

    def post(self, request, slug):
        tag = Tags.objects.get(url_tags__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            context = {
                'form': bound_form,
                'tag': tag
            }
            return render(request, 'post/tag_update_form.html', context)


class PostUpdateView(View):
    def get(self, request, slug):
        post = Post.objects.get(url__iexact=slug)
        bound_form = PostForm(instance=post)
        context = {
            'form': bound_form,
            'post': post
        }
        return render(request, 'post/post_update_form.html', context)

    def post(self, request, slug):
        post = Post.objects.get(url__iexact=slug)
        bound_form = PostForm(request.POST, request.FILES, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {
                'form': bound_form,
                'post': post
            }
            return render(request, 'post/post_update_form.html', context)


class TagDeleteView(View):
    def get(self, request, slug):
        tag = Tags.objects.get(url_tags__iexact=slug)
        bound_form = TagForm(instance=tag)
        context = {
            'form': bound_form,
            'tag': tag
        }
        return render(request, 'post/tag_delete_form.html', context)

    def post(self, request, slug):
        tag = Tags.objects.get(url_tags__iexact=slug)
        tag.delete()
        return redirect(reverse('tags'))


class PostDeleteView(View):
    def get(self, request, slug):
        post = Post.objects.get(url__iexact=slug)
        bound_form = PostForm(instance=post)
        context = {
            'form': bound_form,
            'post': post
        }
        return render(request, 'post/post_delete_form.html', context)

    def post(self, request, slug):
        post = Post.objects.get(url__iexact=slug)
        post.delete()
        return redirect(reverse('posts'))
