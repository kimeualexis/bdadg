# Generated by Django 2.2 on 2019-04-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
