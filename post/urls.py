from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='posts'),
    path('tags/', views.TagsListView.as_view(), name='tags'),
    path('post/create/', views.CreatePostView.as_view(), name='post_create'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag/<str:slug>/update/', views.TagUpdateView.as_view(), name='tag_update_url'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update_url'),
    path('tag/<slug:slug>/delete/', views.TagDeleteView.as_view(), name='tag_delete_url'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete_url'),


]

