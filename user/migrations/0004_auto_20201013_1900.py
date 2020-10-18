# Generated by Django 3.1.1 on 2020-10-13 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20201012_1135'),
        ('user', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartFilm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='created date')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cart')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.film')),
            ],
            options={
                'db_table': 'movie_cart_film',
                'ordering': ['quantity'],
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='film',
            field=models.ManyToManyField(through='user.CartFilm', to='movie.Film'),
        ),
    ]