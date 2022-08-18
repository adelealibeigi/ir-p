from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django.urls import path

from .views import *

urlpatterns = [
    path('list/', UserViewSet.as_view({'get': 'list'})),
    path('create/', UserViewSet.as_view({'post': 'create'})),

    # simpleJWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
