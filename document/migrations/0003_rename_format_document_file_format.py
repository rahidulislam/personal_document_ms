# Generated by Django 4.2.3 on 2023-07-18 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_format'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='format',
            new_name='file_format',
        ),
    ]
