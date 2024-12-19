from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
user_creation_logger = logging.getLogger('user_creation_logger')
User = get_user_model()

@receiver(post_save, sender=User)
def log_creation(sender, instance, created, **kwargs):
    if created:
        user_creation_logger.info(f"User Created with name '{instance.name}'.")
