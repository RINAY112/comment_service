from rest_framework import generics, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @api_view(['GET'])
    def comment_count(request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        count = post.comments.count()
        return Response({'comment_count': count})