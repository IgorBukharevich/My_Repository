# Generated by Django 3.2.15 on 2022-12-24 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20221220_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationvisitors',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hall_time_show', to='mainapp.hall', verbose_name='Зал'),
        ),
    ]
