# Generated by Django 3.1.5 on 2021-01-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
