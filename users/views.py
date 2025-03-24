from rest_framework import generics, status, permissions
from .models import User
from rest_framework.decorators import api_view
import rest_framework.decorators
from rest_framework.response import Response
from .serializers import UserSerializer
from .permissions import IsAdminUserOrReadOnly, IsAdminUserOrSelfOrReadOnly


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrSelfOrReadOnly]

    @api_view(['GET'])
    @rest_framework.decorators.permission_classes([permissions.IsAuthenticated])
    def lightweight_info(request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = {
            'username': user.username,
        }
        return Response(data)