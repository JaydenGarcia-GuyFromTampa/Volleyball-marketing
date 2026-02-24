from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CampaignViewSet, EventViewSet, ExternalApiViewSet

router = DefaultRouter()
router.register("campaigns", CampaignViewSet, basename="campaign")
router.register("events", EventViewSet, basename="event")
router.register("external", ExternalApiViewSet, basename="external")

urlpatterns = [
    path("", include(router.urls)),
]
