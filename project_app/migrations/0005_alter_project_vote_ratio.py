# Generated by Django 4.1.7 on 2023-03-07 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_alter_project_vote_ratio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank='True', default=10, max_length=2, null='True', validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
