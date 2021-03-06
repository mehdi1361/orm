# Generated by Django 3.1.1 on 2020-10-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='created date')),
                ('country', models.CharField(max_length=100)),
                ('last_update', models.DateField()),
            ],
            options={
                'ordering': ['last_update'],
            },
        ),
    ]
