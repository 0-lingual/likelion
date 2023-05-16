from django.shortcuts import render
from .jwt_serializer import SpartaTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class SpartaTokenObtainPairView(TokenObtainPairView):
    serializer_class=SpartaTokenObtainPairSerializer

# 회원가입 구현
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
        
        return res
    
