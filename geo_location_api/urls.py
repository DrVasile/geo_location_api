from django.contrib import admin
from django.urls import include, path
from geo_location_api import views
from rest_framework import routers

from geo_location_api.views import init_plotter

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('plot/', init_plotter),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
