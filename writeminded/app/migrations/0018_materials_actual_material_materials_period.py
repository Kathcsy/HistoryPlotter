# Generated by Django 4.1.3 on 2022-12-12 15:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_merge_20221212_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='actual_material',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='materials',
            name='period',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
