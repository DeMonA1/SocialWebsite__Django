from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile


user_model = get_user_model()

@receiver(post_save, sender=user_model)
def create_profile(sender, instance, **kwargs):
    try:
        Profile.objects.get(user=instance)
    except:
        Profile.objects.create(user=instance)
 