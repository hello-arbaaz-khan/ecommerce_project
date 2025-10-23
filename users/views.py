from django.shortcuts import render
from .serializers import SignupSerializer,LoginSerializer
from rest_framework.views import APIView,Response
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    def post(self,request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User created Successfully'},status=201)
        return Response(serializer.errors,status=400)  
    
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'message':f'Wellcom {user.username}!'})
        return Response(serializer.errors,status=401)
        
class LogoutView(APIView):
    def post(self,request):
        logout(request)
        return Response({'message':'logged out successfully!'},status=200)