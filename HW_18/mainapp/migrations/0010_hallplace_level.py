# Generated by Django 3.2.15 on 2022-12-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20221212_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallplace',
            name='level',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Уровень'),
        ),
    ]
