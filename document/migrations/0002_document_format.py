# Generated by Django 4.2.3 on 2023-07-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='format',
            field=models.CharField(default='pdf', max_length=50),
            preserve_default=False,
        ),
    ]