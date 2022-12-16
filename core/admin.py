from django.contrib import admin

# Register your models here.
from .models import Ong, Post, Comentario, midia

admin.site.register(Ong)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(midia)
