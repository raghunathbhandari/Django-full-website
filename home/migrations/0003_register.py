# Generated by Django 4.1.1 on 2022-09-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_desc_contact_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('emailid', models.CharField(max_length=122)),
                ('addres', models.CharField(max_length=122)),
                ('ocupation', models.CharField(max_length=122)),
                ('date', models.DateField(verbose_name='')),
            ],
        ),
    ]
