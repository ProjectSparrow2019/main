from django.db import models

class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey(Marcas,on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

class Anuncios(models.Model):
    id_anuncio = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=7,decimal_places=2)
    classificacao = models.CharField(max_length=10)

class Resultados(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    id_anuncio = models.ForeignKey(Anuncios, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    predicao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=7,decimal_places=2)
    percentual = models.DecimalField(max_digits=2,decimal_places=2)




# classe para ORM manual do Mongo

class Anuncios_obtidos:
    nome = ''
    autor = ''
    descricao = ''
    preco = 0.0
    predicao = ''
    percentual = 0.0
    link = ''
