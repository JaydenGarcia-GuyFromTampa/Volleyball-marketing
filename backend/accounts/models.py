from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user for volleyball marketing app."""
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ("viewer", "Viewer"),
            ("marketer", "Marketer"),
            ("admin", "Admin"),
        ],
        default="viewer",
    )

    class Meta:
        db_table = "accounts_user"

    def __str__(self):
        return self.email or self.username
