from rest_framework import serializers
from .models import Campaign, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "campaign",
            "title",
            "description",
            "event_date",
            "location",
            "external_id",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


class CampaignSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "start_date",
            "end_date",
            "is_active",
            "created_by",
            "created_at",
            "updated_at",
            "events",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class CampaignWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = (
            "name",
            "slug",
            "description",
            "start_date",
            "end_date",
            "is_active",
        )

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)
