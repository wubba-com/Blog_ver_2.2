from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from django.urls import reverse

from .models import Post, Tags
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class PostListView(ListView):
    """Вывод всех статей"""
    model = Post
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


class TagCreateView(LoginRequiredMixin, CreateView):
    """Создание тега"""
    model = Tags
    form_class = TagForm
    template_name = 'post/tag_create.html'
    raise_exception = True


class CreatePostView(LoginRequiredMixin, CreateView):
    """Создание статьи пользователем"""
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_form.html'
    raise_exception = True


class TagUpdateView(LoginRequiredMixin, View):
    """Изменение тега"""
    raise_exception = True

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


class PostUpdateView(LoginRequiredMixin, View):
    """Изменение поста"""
    raise_exception = True

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


class TagDeleteView(LoginRequiredMixin, View):
    """Удаление тега"""
    raise_exception = True

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


class PostDeleteView(LoginRequiredMixin, View):
    """Удаление поста"""
    raise_exception = True

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


class Search(ListView):

    template_name = 'post/posts_list.html'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return Post.objects.filter(Q(title__icontains=search_query) | Q(body_post__icontains=search_query))