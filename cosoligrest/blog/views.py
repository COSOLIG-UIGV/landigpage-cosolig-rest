from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from django.views.generic import ListView


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
# Create your views here.

class PostView(ListView):
    template_name = 'principal/index.html'
    model = Post
    context_object_name = 'posteo'

    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(evento_activo=True)
        return queryset
