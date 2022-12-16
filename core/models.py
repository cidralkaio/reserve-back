from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

from django.contrib.auth.hashers import make_password


def validate_password(value) -> str:

    return False


class Ong(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, validators=[
                                validate_password])
    image = models.ImageField(upload_to='images', null=True)
    city = models.CharField(max_length=100)
    descricao = models.CharField(
        max_length=1000, null=True, default="sem descrição")
    createdAt = models.DateTimeField(auto_now_add=True)

    is_anonymous = False
    is_authenticated = True

    objects = UserManager()

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Ong, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(Ong, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class midia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(Ong, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    midia = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.autor.name
