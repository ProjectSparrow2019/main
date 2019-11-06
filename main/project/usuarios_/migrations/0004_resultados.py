# Generated by Django 2.2.4 on 2019-08-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_', '0003_anuncios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id_resultado', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('predicao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('percentual', models.DecimalField(decimal_places=2, max_digits=2)),
                ('id_anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios_.Anuncios')),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios_.Marcas')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios_.Produtos')),
            ],
        ),
    ]
