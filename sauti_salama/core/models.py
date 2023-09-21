from django.db import models
from django.contrib.auth.models import User
import uuid 


class MediaFile(models.Model):
    file = models.FileField(upload_to='media_files/')


class SGBVReport(models.Model):
    # Define choices for the type of SGBV incident
    INCIDENT_CHOICES = [
        ('sexual_assault', 'Sexual Assault'),
        ('domestic_violence', 'Domestic Violence'),
        ('harassment', 'Harassment'),
        ('other', 'Other'),
    ]

    # Use UUIDField as the primary key with default value
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)

    media_files = models.ManyToManyField(MediaFile, blank=True)

    def __str__(self):
        return f"Report {self.id} - {self.incident_type} by {self.user.username}"
