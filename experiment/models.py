#-*- coding: utf-8 -*-
from django.db import models
from app_data import AppDataField


class MyModel(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    is_awesome = models.BooleanField(default=False)

    app_data = AppDataField()


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


from django.forms.models import ModelMultipleChoiceField
from app_data import app_registry, AppDataForm, AppDataContainer


class TaggingAppDataForm(AppDataForm):
    public_tags = ModelMultipleChoiceField(Tag.objects.all())
    admin_tags = ModelMultipleChoiceField(Tag.objects.all())

    admin_fieldsets = [
        ('Taggingzs!', {'fields': [('tagging.public_tags', 'tagging.admin_tags')]})
    ]


class TaggingAppDataContainer(AppDataContainer):
    form_class = TaggingAppDataForm

    def tag_string(self):
        print ', '.join(t.name for t in self.public_tags)

app_registry.register('tagging', TaggingAppDataContainer, MyModel)