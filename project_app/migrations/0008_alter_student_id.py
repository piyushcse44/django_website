# Generated by Django 4.1.7 on 2023-03-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
