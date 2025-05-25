from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    def __str__(self):
        return self.email


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    marketing_list_accepted_at = models.DateTimeField(blank=True, null=True)

    @property
    def marketing_list_accepted(self) -> bool:
        return bool(self.marketing_list_accepted_at)
