# Generated by Django 4.1.4 on 2023-01-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiMonitoring', '0002_remove_apimodel_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='apimodel',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]