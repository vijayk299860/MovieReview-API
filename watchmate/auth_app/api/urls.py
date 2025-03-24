from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from auth_app.api.views import registration_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name='register'),
    # path('logout/', logout_view, name='logout'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/introspect/', TokenIntrospectView.as_view(), name='token_introspect'),
]
