from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag

class Blog(models.Model):

    name = models.CharField(max_length=220)
    surname = models.CharField(max_length=520)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
      return self.name + ' - '+ self.surname

