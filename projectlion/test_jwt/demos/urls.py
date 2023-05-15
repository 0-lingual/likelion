from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    )
from django.urls import path
from .views import *
from user.views import SpartaTokenObtainPairView

urlpatterns=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/sparta/token/', SpartaTokenObtainPairView.as_view(), name='sparta_token'),
]