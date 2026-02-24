from django.contrib import admin
from .models import Campaign, Event


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "start_date", "end_date", "created_by", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ("created_by",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "campaign", "event_date", "location", "created_at")
    list_filter = ("campaign",)
    search_fields = ("title", "location")
    raw_id_fields = ("campaign",)
