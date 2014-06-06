# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyModel'
        db.create_table(u'experiment_mymodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('is_awesome', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'experiment', ['MyModel'])


    def backwards(self, orm):
        # Deleting model 'MyModel'
        db.delete_table(u'experiment_mymodel')


    models = {
        u'experiment.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_awesome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['experiment']