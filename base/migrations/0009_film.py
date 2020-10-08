# Generated by Django 3.1.1 on 2020-10-08 08:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tsvector_field


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='created date')),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('description', models.TextField()),
                ('release_year', models.SmallIntegerField()),
                ('rental_duration', models.SmallIntegerField(default=3)),
                ('rental_rate', models.DecimalField(decimal_places=2, default=4.99, max_digits=4)),
                ('length', models.SmallIntegerField()),
                ('replacement_cost', models.DecimalField(decimal_places=2, default=19.99, max_digits=5)),
                ('rating', models.CharField(choices=[('R', 'R'), ('PG-13', 'PG-13'), ('NC-17', 'NC-17')], max_length=5)),
                ('last_update', models.DateField(default=datetime.date(2020, 10, 8))),
                ('special_features', models.TextField()),
                ('fulltext', tsvector_field.SearchVectorField()),
                ('cover', models.ImageField(null=True, upload_to='media/cover')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.language')),
            ],
            options={
                'db_table': 'movie_film',
                'ordering': ['last_update'],
            },
        ),
    ]
