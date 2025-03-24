from rest_framework import generics, status, permissions
from .models import Comment
from rest_framework.decorators import api_view
import rest_framework.decorators
from rest_framework.response import Response
from .serializers import CommentSerializer
from .permissions import IsAuthorOrReadOnly

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    @api_view(['GET'])
    @rest_framework.decorators.permission_classes([permissions.IsAuthenticated])
    def user_comment_count(request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        count = Comment.objects.filter(author=comment.author).count()
        return Response({'user_comment_count': count})