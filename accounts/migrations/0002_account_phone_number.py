# Generated by Django 4.2.7 on 2023-11-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
