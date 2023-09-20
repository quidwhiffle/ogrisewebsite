# Generated by Django 4.0 on 2022-02-16 04:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='resource',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
