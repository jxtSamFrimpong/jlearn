from django.urls import path
from .views import BlogPostListCreate, BlogPostUpdateDelete, HelloWorld, BlogPostList

urlpatterns = [
    path('blogposts/', BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:id>/', BlogPostUpdateDelete.as_view(), name='blogpost-update-delete'),
    path('hello/', HelloWorld.as_view(), name='hello-world'),
    path('blogposts/search/', BlogPostList.as_view(), name='blogpost-search'),
]