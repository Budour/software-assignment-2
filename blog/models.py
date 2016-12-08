from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):

    name = models.CharField(max_length=220)
    surname = models.CharField(max_length=520)

    def __str__(self):
       return self.name + ' - '+ self.surname
