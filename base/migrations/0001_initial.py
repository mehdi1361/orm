# Generated by Django 3.1.1 on 2020-10-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='created date')),
                ('name', models.CharField(max_length=50)),
                ('last_update', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
