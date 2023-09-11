from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(APIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)