# Generated by Django 2.2.7 on 2019-12-07 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191206_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='pieza',
            name='imagenprueba',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]