from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from account.api.serializers import UserSerializer
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):   #### for removing pk requirement it overrides
        return self.request.user




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

   
