from core.models import Post, Ong, midia, Comentario
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password, check_password


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class OngSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(OngSerializer, self).create(validated_data)

    class Meta:
        model = Ong
        fields = "__all__"


class midiaSerializer(ModelSerializer):
    class Meta:
        model = midia
        fields = "__all__"


class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"
