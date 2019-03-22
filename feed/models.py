from django.db import models
from django.conf import settings
from django.utils import timezone


class Offer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    offer_description = models.TextField(null=True)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    service_type = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    start_date = models.DateField()
    deadline = models.DateField()
    request_description = models.TextField(null=True)
    image = models.ImageField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
