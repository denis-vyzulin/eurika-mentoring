from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

# Login, email, password
# get token
# via token, get information about user: Mentor or Mentee
# according to user, provide access to different methods and access
# projects

# Registration
# Mentor or Mentee


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #def get(self, request):
    #    #permission_classes = (IsAuthenticated,)
    #    serializer = UserSerializer(request.user)
    #    return Response(serializer.data)
