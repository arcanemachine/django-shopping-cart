from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    cart = models.JSONField(default=dict)
    cart_modified_at = models.DateTimeField(default=timezone.now)

    first_name = models.CharField(max_length=255, blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=True)
    address1 = models.CharField(max_length=255, blank=False, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=False, null=True)
    zip_code = models.CharField(max_length=255, blank=False, null=True)
    state = models.CharField(max_length=255, blank=False, null=True)
    country = models.CharField(max_length=255, blank=False, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"user '{self.user.username}'"

    def get_absolute_url(self):
        return self.user.get_absolute_url()

    def save(self, *args, **kwargs):
        if self.pk:
            old_object_instance = Profile.objects.get(pk=self.pk)
            if old_object_instance.cart != self.cart:
                self.cart_modified_at = timezone.now()
        super().save(*args, **kwargs)
