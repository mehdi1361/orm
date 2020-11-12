from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_auto_20201106_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='created date')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'movie_director',
            },
        ),

    ]
