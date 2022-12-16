
from rest_framework.viewsets import ModelViewSet
from core.models import Post, Ong, midia, Comentario
from core import serializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, User):
        token = super().get_token(User)

        # Add custom claims
        token['id'] = User.id
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializer


class OngViewSet(ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = serializer.OngSerializer
    permission_classe = [IsAuthenticated]


class midiaViewSet(ModelViewSet):
    queryset = midia.objects.all()
    serializer_class = serializer.midiaSerializer


class ComentariosViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = serializer.ComentariosSerializer
