# Generated by Django 5.1 on 2024-11-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=100)),
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('scharacter', models.CharField(max_length=100)),
            ],
        ),
    ]
