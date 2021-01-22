from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    cart = models.JSONField(default=dict)

    def __str__(self):
        return f"user '{self.user.username}'"

    def get_absolute_url(self):
        return self.user.get_absolute_url()
