# Generated by Django 3.1.3 on 2021-01-02 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment1')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to='blog.post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
