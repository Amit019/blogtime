# Generated by Django 3.1.3 on 2020-12-31 07:33

import ckeditor_uploader.fields
from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0002_auto_20201229_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
