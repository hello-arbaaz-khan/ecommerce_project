from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        extra_kwargs = {'password':{'write_only':True}}        
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)
    def validate(self,data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        # if user not provide password
        if not password:
            raise serializers.ValidationError('Password is required to login')
        # if user wants to login with email
        if email:
            try:
                user_obj = User.objects.get(email=email)
                username = user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError('Not account found with this email')
        # if user wants to login with username
        if not username:
            raise serializers.ValidationError('Username or Email is required to login')
        user = authenticate(username=username,password=password)
        # check if user is valid and active
        if user and user.is_active:
           refresh = RefreshToken.for_user(user)
           data["user"] = user
           data["message"] = f"Welcome {user.username}!"
           data["refresh"] = str(refresh)
           data["access"] = str(refresh.access_token)
           return data
        raise serializers.ValidationError('Invalid Credentials')