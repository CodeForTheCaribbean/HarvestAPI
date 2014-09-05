# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Farmer'
        db.create_table(u'farmers_farmer', (
            ('farmer_idx', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
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
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(default='1', related_name='farmers', null=True, to=orm['auth.User'])),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'farmers', ['Farmer'])

        # Adding model 'Receipt'
        db.create_table(u'farmers_receipt', (
            ('receipt_no', self.gf('django.db.models.fields.CharField')(default='', max_length=100, primary_key=True)),
            ('rec_range1', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('rec_range2', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('investigation_status', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True)),
            ('farmer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['farmers.Farmer'])),
        ))
        db.send_create_signal(u'farmers', ['Receipt'])

        # Adding model 'Farm'
        db.create_table(u'farmers_farm', (
            ('farmer_idx', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('farm_address', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('farm_id', self.gf('django.db.models.fields.CharField')(default='', max_length=100, primary_key=True)),
            ('parish', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('district', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('extension', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('farm_size', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('long', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('farm_status', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('farmer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['farmers.Farmer'])),
        ))
        db.send_create_signal(u'farmers', ['Farm'])

        # Adding model 'Crop'
        db.create_table(u'farmers_crop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crop_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('common_name', self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True)),
            ('estimated_vol', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('variety', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('plant_date', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('count', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('area', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('exp_date', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True)),
            ('farm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['farmers.Farm'])),
        ))
        db.send_create_signal(u'farmers', ['Crop'])


    def backwards(self, orm):
        # Deleting model 'Farmer'
        db.delete_table(u'farmers_farmer')

        # Deleting model 'Receipt'
        db.delete_table(u'farmers_receipt')

        # Deleting model 'Farm'
        db.delete_table(u'farmers_farm')

        # Deleting model 'Crop'
        db.delete_table(u'farmers_crop')


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
        u'farmers.crop': {
            'Meta': {'ordering': "('crop_name',)", 'object_name': 'Crop'},
            'area': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True'}),
            'count': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'crop_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'estimated_vol': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'exp_date': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'farm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmers.Farm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plant_date': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'variety': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'})
        },
        u'farmers.farm': {
            'Meta': {'ordering': "('district',)", 'object_name': 'Farm'},
            'district': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'farm_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'farm_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'primary_key': 'True'}),
            'farm_size': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'farm_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'farmer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmers.Farmer']"}),
            'farmer_idx': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'lat': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'long': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True'}),
            'parish': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'farmers.farmer': {
            'Meta': {'ordering': "('last_updated',)", 'object_name': 'Farmer'},
            'agri_activity': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True'}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'cell_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'farmer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'primary_key': 'True'}),
            'farmer_idx': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'related_name': "'farmers'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'res_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'}),
            'res_parish': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'tel_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'verified_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'null': 'True'})
        },
        u'farmers.receipt': {
            'Meta': {'ordering': "('last_updated',)", 'object_name': 'Receipt'},
            'farmer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmers.Farmer']"}),
            'investigation_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'rec_range1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'rec_range2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'receipt_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'primary_key': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['farmers']