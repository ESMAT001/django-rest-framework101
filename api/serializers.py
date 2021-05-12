from rest_framework import serializers
from .models import Post , like

class PostSerializer(serializers.ModelSerializer)
    class Meta:
        model = Post
        fields = ['id', 'title','url','poster','likes','created'] 