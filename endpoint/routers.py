from rest_framework.routers import DefaultRouter
from .views import StringViewSet


router = DefaultRouter()
router.register(r'strings', StringViewSet)
