from django.shortcuts import render
from .serializers import SignupSerializer,LoginSerializer
from rest_framework.views import APIView,Response
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            print("Signup API hit!")
            return Response({'message': 'User created successfully'}, status=201)
        return Response(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=401)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message':'logged out successfully!'},status=200)