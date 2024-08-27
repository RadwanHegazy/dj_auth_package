from .serializers import LoginSerializer, RegisterSerializer, ChangePasswordSerializer, ResetPassword_SentEmailSerializer, ResetPasswordSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions

class LoginView (CreateAPIView) : 
    serializer_class = LoginSerializer

class RegisterView (CreateAPIView) : 
    serializer_class = RegisterSerializer

class ChangePassword (CreateAPIView) : 
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = {
            'user' : self.request.user
        }
        return context

class ResetPasswordOTP(CreateAPIView)  :
    serializer_class = ResetPassword_SentEmailSerializer


class ResetPassowrd (CreateAPIView):
    serializer_class = ResetPasswordSerializer
