from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'url', 'titulo', 'contenido','fecha_evento','fecha_evento','banner_grande','lugar')