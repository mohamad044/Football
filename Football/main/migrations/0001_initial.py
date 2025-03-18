# Generated by Django 5.0.1 on 2025-03-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('len_clubs', models.SmallIntegerField(default=20)),
                ('country', models.CharField(max_length=1024)),
            ],
        ),
    ]
