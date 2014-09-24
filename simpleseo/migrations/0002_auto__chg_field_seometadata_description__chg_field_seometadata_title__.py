# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SeoMetadata.description'
        db.alter_column('seo_metadata', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'SeoMetadata.title'
        db.alter_column('seo_metadata', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'SeoMetadata.path'
        db.alter_column('seo_metadata', 'path', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'SeoMetadata.description'
        db.alter_column('seo_metadata', 'description', self.gf('django.db.models.fields.CharField')(max_length=155))

        # Changing field 'SeoMetadata.title'
        db.alter_column('seo_metadata', 'title', self.gf('django.db.models.fields.CharField')(max_length=68))

        # Changing field 'SeoMetadata.path'
        db.alter_column('seo_metadata', 'path', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simpleseo.seometadata': {
            'Meta': {'ordering': "('path', 'lang_code')", 'unique_together': "(('path', 'lang_code'),)", 'object_name': 'SeoMetadata', 'db_table': "'seo_metadata'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '2'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['simpleseo']