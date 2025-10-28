from django.shortcuts import render
from .serializers import SignupSerializer,LoginSerializer
from rest_framework.views import APIView,Response
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = data['user']
            return Response({
                'message': f'Welcome {user.username}!',
                'refresh': data['refresh'],
                'access': data['access']
            })
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'logged out successfully!'}, status=status.HTTP_200_OK)