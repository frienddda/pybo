# Generated by Django 4.0.3 on 2022-03-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_questioncount'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]
