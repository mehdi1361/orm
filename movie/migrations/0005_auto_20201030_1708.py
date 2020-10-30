# Generated by Django 3.1.1 on 2020-10-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20201012_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='fulltext',
        ),
        migrations.RemoveField(
            model_name='film',
            name='special_features',
        ),
        migrations.AddField(
            model_name='film',
            name='fa_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='fa_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.CharField(choices=[('R', 'R'), ('PG-13', 'PG-13'), ('NC-17', 'NC-17')], default='R', max_length=5),
        ),
    ]