from rest_framework import generics, status
from .models import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @api_view(['GET'])
    def user_comment_count(request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        count = Comment.objects.filter(author=comment.author).count()
        return Response({'user_comment_count': count})