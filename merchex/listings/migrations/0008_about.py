# Generated by Django 4.1.4 on 2022-12-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_band_year_formed_alter_listing_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
