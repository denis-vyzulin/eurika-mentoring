# Generated by Django 3.2.15 on 2022-08-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evrika', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(max_length=30, verbose_name='patronymic'),
        ),
    ]