from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
# Create your views here.
