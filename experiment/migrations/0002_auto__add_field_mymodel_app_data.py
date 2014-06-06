# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MyModel.app_data'
        db.add_column(u'experiment_mymodel', 'app_data',
                      self.gf('app_data.fields.AppDataField')(default='{}'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MyModel.app_data'
        db.delete_column(u'experiment_mymodel', 'app_data')


    models = {
        u'experiment.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            'app_data': ('app_data.fields.AppDataField', [], {'default': "'{}'"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_awesome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['experiment']