# Generated by Django 2.2.12 on 2020-04-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useridealtype',
            name='age_from',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useridealtype',
            name='age_to',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
