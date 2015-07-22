from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('cosoligrest.urls', namespace='cosoligrest')),
)