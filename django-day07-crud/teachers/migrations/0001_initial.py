# Generated by Django 4.1.5 on 2023-01-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('nname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('memo', models.TextField()),
            ],
        ),
    ]
