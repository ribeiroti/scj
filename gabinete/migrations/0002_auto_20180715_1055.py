# Generated by Django 2.0.5 on 2018-07-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gabinete', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
