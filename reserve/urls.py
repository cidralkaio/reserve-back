from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from core.views import midiaViewSet, OngViewSet, PostViewSet, ComentariosViewSet, MyTokenObtainPairView

router = DefaultRouter()
router.register(r"Comentarios", ComentariosViewSet)
router.register(r"midia", midiaViewSet)
router.register(r"Ong", OngViewSet)
router.register(r"Post", PostViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
