# Generated by Django 4.2.5 on 2023-09-24 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
