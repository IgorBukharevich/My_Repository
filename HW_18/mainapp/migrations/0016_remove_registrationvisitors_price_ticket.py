# Generated by Django 3.2.15 on 2022-12-24 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_registrationvisitors_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationvisitors',
            name='price_ticket',
        ),
    ]