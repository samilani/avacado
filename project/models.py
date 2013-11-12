from django.db import models
from django.contrib.auth.models import User, Group
from idea.models import Idea

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    idea = models.OneToOneField(Idea)
    def __unicode__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project)
    summery = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    comment = models.TextField()

    def __unicode__(self):
        return self.summery


class UserProfile(models.Model):
    user = models.OneToOneField(User)


    def __unicode__(self):
        return self.user.username





