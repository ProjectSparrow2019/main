# Generated by Django 2.2.4 on 2019-08-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_', '0004_resultados'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncios',
            name='classificacao',
            field=models.CharField(default='falso', max_length=10),
            preserve_default=False,
        ),
    ]
