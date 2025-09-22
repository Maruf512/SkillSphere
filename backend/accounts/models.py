from django.db import models
from django.conf import settings


class Account(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to="uploads/avatars/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False

    def __str__(self):
        return self.email
    
    @property
    def avatar_url(self):
        if self.avatar:
            return f"{settings.WEBSITE_URL}/{self.avatar.url}"
        else:
            return 'failed'