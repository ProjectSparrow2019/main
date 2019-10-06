from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from usuarios_.models import *
import pymongo
from django.db.models import Avg, Max, Min, Sum, Value
from django.db.models.functions import Coalesce

class IA:
    #Como tomar decisoes!
    #Nome do produto =>     tem palavra do dicionario? Sim = 1, nao = 0
    #Nome do author =>      e oficial? Sim = 1, nao = 0
    #Preco =>               mais caro do que o original? (supondo que o original seja 1000) Sim = 1, nao = 0
    #Descricao =>           tem palavra do dicionario? Sim = 1, nao = 0
    classificacao = []
    palavras_preditivas = ['aa','aaa','réplica','replica','primeira','linha']
    sklearn = LinearSVC()
    anuncios =[[]]

    def predict(self, produto_obtido, marca):
        preco_minimo = Anuncios.objects.all().aggregate(the_min=Coalesce(Min('preco'), Value(0)))['the_min']
        lista = []

        lista.append(self.countWords(produto_obtido.nome))

        if(produto_obtido.autor == marca):            #autor
                lista.append(0)
        else:
            lista.append(1)
                
        if(produto_obtido.preco < preco_minimo):                 #preco
            lista.append(1)
        else:
            lista.append(0)

        lista.append(self.countWords(produto_obtido.descricao))    #descricao

        p = self.sklearn.predict([lista])
        
        if(p == 1):
            return 'falso'
        else:
            return 'verdadeiro'

    def connectMongo():
        client = pymongo.MongoClient("mongodb://localhost:3305/")
        return client['sparrow']

    def find_got_products(database, produto):
        collection = self.connectMongo()['anuncios_obtidos']
        query = {"nome" : produto}
        return collection.find(query)

    def trainning(self,anuncios):
        self.storage(anuncios)
        for i in self.anuncios:
            if len(i) < 1:
                self.anuncios.remove(i)
        self.sklearn.fit(self.anuncios,self.classificacao)

    def countWords(self,text):
        splitted = text.split(" ")
        for i in splitted:
            if(i.lower() in self.palavras_preditivas):
                return 1
        return 0

    def storage(self, anuncios):
        preco_minimo = Anuncios.objects.all().aggregate(the_min=Coalesce(Min('preco'), Value(0)))['the_min']
        for i in anuncios:
            lista = []
            lista.append(self.countWords(i.nome))         #nome

            if(i.autor == i.id_marca.nome):            #autor
                lista.append(0)
            else:
                lista.append(1)

            if(i.preco < preco_minimo):                 #preco
                lista.append(1)
            else:
                lista.append(0)

            lista.append(self.countWords(i.descricao))    #descricao

            self.anuncios.append(lista)

            if(i.classificacao == 'falso'):             #classificacao
                self.classificacao.append(1)
            else:
                self.classificacao.append(0)
            