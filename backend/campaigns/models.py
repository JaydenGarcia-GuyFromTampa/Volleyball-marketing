from django.db import models
from django.conf import settings


class Campaign(models.Model):
    """Marketing campaign for volleyball events."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="campaigns",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "campaigns_campaign"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Event(models.Model):
    """Volleyball event tied to a campaign."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=300, blank=True)
    external_id = models.CharField(max_length=100, blank=True, db_index=True)  # from external API
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "campaigns_event"
        ordering = ["event_date"]

    def __str__(self):
        return self.title
