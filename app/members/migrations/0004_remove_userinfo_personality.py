# Generated by Django 2.2.12 on 2020-04-15 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20200415_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='personality',
        ),
    ]
