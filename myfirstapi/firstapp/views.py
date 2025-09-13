from django.shortcuts import render
from rest_framework import generics, status
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
    
class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', "")

        if title:
            blogposts = BlogPost.objects.filter(title__icontains=title)
        else:
            blogposts = BlogPost.objects.all()
        
        serializer = BlogPostSerializer(blogposts, many=True)
        if len(serializer.data) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)