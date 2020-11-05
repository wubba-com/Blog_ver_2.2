from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='posts'),
    path('tags/', views.TagsListView.as_view(), name='tags'),
    path('post/create/', views.CreatePostView.as_view(), name='post_create'),
    path('tags/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]

