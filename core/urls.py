from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include("poll.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth', include('rest_framework.urls'))

    # apart settings for JWT auth

    # from rest_framework_simplejwt.views import (
    #     TokenObtainPairView,
    #     TokenRefreshView, TokenVerifyView,
    # )
    # path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]