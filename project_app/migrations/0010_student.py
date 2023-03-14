# Generated by Django 4.1.7 on 2023-03-14 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0009_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
            ],
        ),
    ]