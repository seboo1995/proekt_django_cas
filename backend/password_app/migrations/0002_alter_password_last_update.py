# Generated by Django 4.0.5 on 2022-06-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='last_update',
            field=models.DateTimeField(null=True),
        ),
    ]