# Generated by Django 3.1.3 on 2021-01-01 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
    ]
