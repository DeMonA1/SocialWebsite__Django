from django.db import models
from django.conf import settings

# Create your models here.

class Actions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='actions',
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']