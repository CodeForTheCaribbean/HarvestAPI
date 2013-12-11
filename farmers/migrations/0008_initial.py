# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Receipt'
        db.create_table(u'farmers_receipt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('farmer_idx', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('receipt_no', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('rec_range1', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('rec_range2', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('investigation_status', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True)),
        ))
        db.send_create_signal(u'farmers', ['Receipt'])

        # Adding model 'Farmer'
        db.create_table(u'farmers_farmer', (
            ('farmer_idx', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
            ('farmer_id', self.gf('django.db.models.fields.CharField')(default='', max_length=100, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('res_address', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True)),
            ('res_parish', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True)),
            ('tel_number', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True)),
            ('cell_number', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True)),
            ('verified_status', self.gf('django.db.models.fields.CharField')(default='', max_length=3, null=True)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')()),
            ('agri_activity', self.gf('django.db.models.fields.CharField')(default='', max_length=150, null=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(default='1', related_name='farmers', to=orm['auth.User'])),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('receipts', self.gf('django.db.models.fields.related.ForeignKey')(related_name='farmers', null=True, to=orm['farmers.Receipt'])),
        ))
        db.send_create_signal(u'farmers', ['Farmer'])


    def backwards(self, orm):
        # Deleting model 'Receipt'
        db.delete_table(u'farmers_receipt')

        # Deleting model 'Farmer'
        db.delete_table(u'farmers_farmer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmers.farmer': {
            'Meta': {'ordering': "('last_updated',)", 'object_name': 'Farmer'},
            'agri_activity': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True'}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'cell_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'farmer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'primary_key': 'True'}),
            'farmer_idx': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'related_name': "'farmers'", 'to': u"orm['auth.User']"}),
            'receipts': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'farmers'", 'null': 'True', 'to': u"orm['farmers.Receipt']"}),
            'res_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'}),
            'res_parish': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'tel_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'verified_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'null': 'True'})
        },
        u'farmers.receipt': {
            'Meta': {'ordering': "('last_updated',)", 'object_name': 'Receipt'},
            'farmer_idx': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigation_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'rec_range1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'rec_range2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'receipt_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'remarks': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['farmers']