from django.contrib import admin
from django.urls import path, include
from api.views import ClienteViewSet, VeiculoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'veiculo',VeiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
