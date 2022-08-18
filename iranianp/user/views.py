# Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .permissions import UserPermission
from .serializers import UserCreateSerializer, UserListSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [UserPermission]
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action=='list':
            return UserListSerializer
        elif self.action=='create':
            return UserCreateSerializer

    def list(self, request):
        return Response(data=self.get_serializer(self.queryset, many=True).data,
            status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        password = make_password(self.request.data['password'])
        if serializer.is_valid():
            serializer.save(password=password)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
