# Generated by Django 4.0.1 on 2022-01-14 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
