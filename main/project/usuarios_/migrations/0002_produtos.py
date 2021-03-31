# Generated by Django 2.2.4 on 2019-08-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios_.Marcas')),
            ],
        ),
    ]