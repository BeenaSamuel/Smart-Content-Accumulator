# Generated by Django 4.1.7 on 2023-06-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
