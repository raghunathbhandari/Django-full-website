# Generated by Django 4.1.1 on 2022-09-08 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='addres',
            new_name='address',
        ),
        migrations.AddField(
            model_name='register',
            name='details',
            field=models.TextField(default=django.utils.timezone.now, verbose_name=''),
            preserve_default=False,
        ),
    ]
