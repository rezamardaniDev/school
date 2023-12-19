from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course
from django.utils import timezone

@receiver(post_save, sender=Course)
def check_registration_date(sender, instance, **kwargs):
    if instance.end_registration_date < timezone.now():
        instance.is_active = False
        instance.save()
