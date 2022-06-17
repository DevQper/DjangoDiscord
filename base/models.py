from cgitb import text
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.




class Topic(models.Model):

    name = models.CharField(("Topic name"), max_length=150)

    class Meta:
        verbose_name = ("Topic")
        verbose_name_plural = ("Topics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Topic_detail", kwargs={"pk": self.pk})


class Room(models.Model):
    
    host = models.ForeignKey(User, verbose_name=("Host"), on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey("Topic", verbose_name=("Topic"), on_delete=models.SET_NULL, null=True)
    name = models.CharField(("Name"), max_length=150)
    description = models.TextField(("Description"), null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True, verbose_name=("Participants"))
    updated = models.DateTimeField(("Updated"), auto_now=True, auto_now_add=False)
    created = models.DateTimeField(("Created"), auto_now=False, auto_now_add=True)


    

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("room")
        verbose_name_plural = ("rooms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})


class Message(models.Model):

    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    room = models.ForeignKey("Room", verbose_name=("Room"), on_delete=models.CASCADE) 
    body = models.TextField(("Message body"))
    updated = models.DateTimeField(("Updated"), auto_now=True, auto_now_add=False) 
    created = models.DateTimeField(("Created"), auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})