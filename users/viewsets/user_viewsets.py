from rest_framework import viewsets
from users.models import UserModel
from users.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer