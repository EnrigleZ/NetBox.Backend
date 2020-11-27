from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import NetBoxUserCreate, AuthTest, NetBoxTokenObtainPairView

urlpatterns = [
    path('token', NetBoxTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('test', AuthTest.as_view(), name='auth_test'),
    path('register', NetBoxUserCreate.as_view(), name="create_user")
]
