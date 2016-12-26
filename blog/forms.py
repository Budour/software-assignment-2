from django import forms
from .models import Blog
# from django.db import models


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["name", "surname", "tags"]

