# Generated by Django 3.2.5 on 2022-05-10 18:20

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]