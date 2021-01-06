# Generated by Django 3.1.3 on 2021-01-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210104_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
