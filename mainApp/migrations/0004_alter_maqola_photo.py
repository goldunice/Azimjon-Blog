# Generated by Django 4.2.7 on 2023-11-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_maqola_delete_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqola',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
