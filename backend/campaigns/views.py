from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Campaign, Event
from .serializers import CampaignSerializer, CampaignWriteSerializer, EventSerializer
from .services import call_external_api


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    permission_classes = ()  # use default from settings (IsAuthenticated)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return CampaignWriteSerializer
        return CampaignSerializer

    def get_queryset(self):
        return Campaign.objects.select_related("created_by").prefetch_related("events")


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.select_related("campaign")


class ExternalApiViewSet(viewsets.ViewSet):
    """Example endpoint that uses external API (stub)."""
    permission_classes = ()

    def list(self, request):
        data = call_external_api("ping") or {"message": "External API not configured"}
        return Response(data)
