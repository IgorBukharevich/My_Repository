# Generated by Django 3.2.15 on 2022-12-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_hallplace_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallplace',
            name='level',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Уровень'),
        ),
    ]
