from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


USER_PROFILE_DATA = (
    'alias',
    'bio',
)


class UserProfile(models.Model):
    """
    Extra data for user. (Adding new filed here make sure that you added its
    name to USER_PROFILE_DATA)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=250)
    bio = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    userFrom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    userTo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipient')
    feedback_text = models.TextField(null=True, blank=True)
    feedback_for_provider = models.BooleanField(default=True);
    grade = models.SmallIntegerField()

    def publish(self):
        self.save()