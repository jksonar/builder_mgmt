# Generated by Django 5.2.1 on 2025-05-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('half_day', 'Half Day'), ('absent', 'Absent')], max_length=20)),
            ],
        ),
    ]
