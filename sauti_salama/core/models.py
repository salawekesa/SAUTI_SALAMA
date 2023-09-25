from django.db import models
from django.contrib.auth.models import User, AbstractUser

import uuid 
    

# class MediaFile(models.Model):
#     file = models.FileField(upload_to='media_files/')

# class Entry(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", 'Admin'
#         SURVIVOR = "SURVIVOR", 'Admin'
#         LEGAL = "LEGAL", 'Legal Councel'
#         HEALTH = "HEALTH", "Health EXpert"
    
#     base_role = Role.ADMIN

#     role = models.CharField(max_length=50, choices=Role.choices)

#     def save(self, *arg, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)

        
class SGBVReport(models.Model):
    INCIDENT_CHOICES = [
        ('sexual_assault', 'Sexual Assault'),
        ('domestic_violence', 'Domestic Violence'),
        ('harassment', 'Harassment'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True) 


    # media_files = models.ManyToManyField(MediaFile, blank=True)

    def __str__(self):
        return f"Sautisalama {self.id} - {self.incident_type} by {self.user.username}"


class Progress(models.Model):
    report = models.OneToOneField(SGBVReport, on_delete=models.CASCADE)
    step_1 = models.BooleanField(default=False)
    step_2 = models.BooleanField(default=False)
    step_3 = models.BooleanField(default=False)