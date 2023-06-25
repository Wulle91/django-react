from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def logout_route(request):
    response = Response()
    response.set_cookie(
        key='JWT_AUTH_COOKIE_NAME',
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite='None',
        secure=True,
    )
    response.set_cookie(
        key='JWT_AUTH_REFRESH_COOKIE_NAME',
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite='None',
        secure=True,
    )
    
    return response

