from rest_framework import serializers
from .models import Profile, User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','username', 'password','role',)
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        Profile.objects.get_or_create(user=user)
        return user
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        access = refresh.access_token
        user_data = {
            "username": instance.username,

        }
        access["user"]=user_data
        data.update({
            "refresh": str(refresh),
            "access": str(access),
        })

        return data


class LoginSerializer(TokenObtainPairSerializer):
    username_field = 'username'

