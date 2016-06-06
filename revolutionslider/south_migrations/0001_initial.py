# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'revolutionslider_slide', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('slide_text', self.gf('django.db.models.fields.CharField')(max_length=2500, null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.IntegerField')(default=1000, null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.IntegerField')(default=5000, null=True)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(default=100, null=True)),
            ('position_x', self.gf('django.db.models.fields.IntegerField')(default=477, null=True)),
            ('position_y', self.gf('django.db.models.fields.IntegerField')(default=180, null=True)),
            ('easing', self.gf('django.db.models.fields.CharField')(default=('OutBack', 'easeOutBack'), max_length=25)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='slide', null=True, to=orm['revolutionslider.Slider'])),
        ))
        db.send_create_signal(u'revolutionslider', ['Slide'])

        # Adding model 'Slider'
        db.create_table(u'revolutionslider_slider', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('master_start', self.gf('django.db.models.fields.IntegerField')(default=1000, blank=True)),
            ('master_end', self.gf('django.db.models.fields.IntegerField')(default=5000, null=True)),
            ('master_speed', self.gf('django.db.models.fields.IntegerField')(default=300, null=True)),
        ))
        db.send_create_signal(u'revolutionslider', ['Slider'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'revolutionslider_slide')

        # Deleting model 'Slider'
        db.delete_table(u'revolutionslider_slider')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'revolutionslider.slide': {
            'Meta': {'object_name': 'Slide', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'easing': ('django.db.models.fields.CharField', [], {'default': "('OutBack', 'easeOutBack')", 'max_length': '25'}),
            'end': ('django.db.models.fields.IntegerField', [], {'default': '5000', 'null': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position_x': ('django.db.models.fields.IntegerField', [], {'default': '477', 'null': 'True'}),
            'position_y': ('django.db.models.fields.IntegerField', [], {'default': '180', 'null': 'True'}),
            'slide_text': ('django.db.models.fields.CharField', [], {'max_length': '2500', 'null': 'True', 'blank': 'True'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'slide'", 'null': 'True', 'to': u"orm['revolutionslider.Slider']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {'default': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'revolutionslider.slider': {
            'Meta': {'object_name': 'Slider', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'master_end': ('django.db.models.fields.IntegerField', [], {'default': '5000', 'null': 'True'}),
            'master_speed': ('django.db.models.fields.IntegerField', [], {'default': '300', 'null': 'True'}),
            'master_start': ('django.db.models.fields.IntegerField', [], {'default': '1000', 'blank': 'True'})
        }
    }

    complete_apps = ['revolutionslider']