from rest_framework import serializers
from .models import Post , Like

class PostSerializer(serializers.ModelSerializer):

    likes = serializers.SerializerMethodField()

    def get_likes(self,post):
        return Like.objects.filter(post=post).count()
    class Meta:
        model = Post
        fields = ['id', 'title','url','poster','created_at','likes'] 


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id']