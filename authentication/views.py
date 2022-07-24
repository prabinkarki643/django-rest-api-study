from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from authentication.classes.custom_auth_token import BearerTokenAuthentication
# Create your views here.


@api_view(["GET"])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_details_from_token(request):
    content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            'details':{
                "username":request.user.username,
                "user_id":request.user.id
            }
        }
    return Response(content)