# Generated by Django 3.0.4 on 2020-03-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200329_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=60, null=True, unique=True),
        ),
    ]