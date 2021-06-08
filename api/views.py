from django.shortcuts import render
from rest_framework import generics , permissions ,mixins
from rest_framework.exceptions import  ValidationError
from .models import Post ,Like
from .serializers import PostSerializer , LikeSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]


class likeCreate(generics.CreateAPIView,mixins.DestroyModelMixin):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        if not post.exists():
            raise ValidationError("no post!")       
        return Like.objects.filter(liker=user,post=post)

    def perform_create(self,serializer):
        print("_____________",self.kwargs['pk'])
        
        if self.get_queryset().exists():
            raise ValidationError("no post!")  
        post=Post.objects.filter(pk=self.kwargs['pk'])
        serializer.save(liker=self.request.user,post=post)