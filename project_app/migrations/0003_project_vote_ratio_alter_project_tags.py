# Generated by Django 4.1.7 on 2023-03-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_tag_project_vote_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank='True', default=0, null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='project',
            name='Tags',
            field=models.ManyToManyField(blank='True', to='project_app.tag'),
        ),
    ]
