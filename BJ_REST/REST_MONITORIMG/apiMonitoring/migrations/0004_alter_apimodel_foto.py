# Generated by Django 4.1.4 on 2023-01-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiMonitoring', '0003_apimodel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimodel',
            name='foto',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
