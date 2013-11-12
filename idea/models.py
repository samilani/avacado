from django.db import models
from django.contrib.auth.models import User
class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User)
    available = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title