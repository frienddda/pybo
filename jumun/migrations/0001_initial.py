# Generated by Django 3.1.5 on 2022-01-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jumun_T',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumun_date', models.DateTimeField()),
                ('jumun_id', models.CharField(max_length=30)),
                ('jumun_name', models.CharField(max_length=30)),
                ('consumer', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('prd_name', models.CharField(max_length=50)),
                ('option', models.CharField(max_length=150)),
                ('quantity', models.SmallIntegerField(verbose_name='수량')),
                ('d_price', models.IntegerField(verbose_name='도매가격')),
                ('memo', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, max_length=30)),
                ('exposure', models.CharField(default='O', max_length=10)),
            ],
        ),
    ]
