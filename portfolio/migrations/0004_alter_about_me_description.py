# Generated by Django 5.0.2 on 2025-02-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_about_me_project_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
