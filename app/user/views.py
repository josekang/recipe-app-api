from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from core.models import User
from .serializers import UserSerializer, AuthTokenSerializer

# Create your views here.


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        super(UserListCreateView, self).list(request, *args, **kwargs)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response = {
            'status': status.HTTP_200_OK,
            'message': 'All user details rettieved successfully',
            'data': data
        }
        
        return Response(response)
    
    def create(self, request, *args, **kwargs):
        super(UserListCreateView, self).create(request, *args, **kwargs)
        response = {
            'status': status.HTTP_201_CREATED,
            'message': 'User created successfully',
            'data': request.data
        }
        
        return Response(response)
        

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ManageUserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'User account retrieved successfully',
            'data': data
        }
        
        return Response(response)
    
    def patch(self, request, *args, **kwargs):
        super(ManageUserRetrieveUpdateView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'User account updated successfully',
            'data': data
        }
        return Response(response)