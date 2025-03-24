from rest_framework.decorators import api_view,permission_classes
from auth_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

@api_view(['POST'])
@permission_classes([AllowAny]) 
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "registratin successful"
            data['username'] = account.username
            data['email'] = account.email
            # data['token'] = account.auth_token.key 
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
             
        else:
            data['error'] = serializer.errors
        return Response(data)
    
# @api_view(['POST'])
# def logout_view(request):
#     try:
#         request.user.auth_token.delete()
#         return Response({"message": "Logged out successfully"})
#     except Exception as e:
#         return Response({"error": str(e)})