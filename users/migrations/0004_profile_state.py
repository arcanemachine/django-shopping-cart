# Generated by Django 3.1.5 on 2021-01-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210123_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
    ]