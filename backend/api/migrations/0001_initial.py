# Generated by Django 4.2.5 on 2023-11-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(verbose_name='date and time of event')),
                ('cancelled', models.BooleanField(default=False, verbose_name='event is cancelled')),
                ('max_attendees', models.IntegerField()),
            ],
        ),
    ]
