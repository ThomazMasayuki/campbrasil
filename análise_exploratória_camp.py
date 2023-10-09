import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import lance as lance

#Importação das bases
campcart = pd.read_csv("campeonato-brasileiro-cartoes.csv")
campestat = pd.read_csv("campeonato-brasileiro-estatisticas-full.csv")
campbrasfull = pd.read_csv("campeonato-brasileiro-full.csv")
campbrasgols = pd.read_csv("campeonato-brasileiro-gols.csv")

#Verificando as colunas de cada dataset
campcart.columns
campestat.columns
campbrasfull.columns
campbrasgols.columns

campcart.dtypes
campestat.dtypes
campbrasfull.dtypes
campbrasgols.dtypes

#Verificando se possuem valores vazios
campcart.isnull().sum()
campestat.isnull().sum()
campbrasfull.isnull().sum()
campbrasgols.isnull().sum()

#Trazendo uma análise a partir das vitórias, verificamos o maior vencedor durante todo esse tempo
campbrasfull["vencedor"].value_counts(ascending=False).head(5)

#Tendo essas informações, podemos perceber que só de empate deu 2123 e os primeiros colocados foram, São Paulo, Flamengo e Santos, com 351, 335 e 329 respectivamente;
campbrasfull["vencedor"].value_counts(ascending=False).head(5).plot.barh()

#Verificar informaçãn por mandante e visitante e dessa relação, verificar a quantidade de vitórias e derrotas
campbrasfull["mandante"].value_counts(ascending=False).head(5)
campbrasfull["visitante"].value_counts(ascending=False).head(5)
campbrasfull["mandante"].value_counts(ascending=False).head(5).plot.barh()
campbrasfull["visitante"].value_counts(ascending=False).head(5).plot.barh()

#Quantos jogos dos mandantes, quantos foram vencedores
campbrasfull.groupby(["mandante", "vencedor", "data"]).sum().reset_index()

#Mandante por estados e visitante por estado
campbrasfull["mandante_Estado"].value_counts(ascending=False).head(5)
campbrasfull["visitante_Estado"].value_counts(ascending=False).head(5)
campbrasfull["mandante_Estado"].value_counts(ascending=False).head(10).plot.barh()
campbrasfull["visitante_Estado"].value_counts(ascending=False).head(10).plot.barh()

#Rankinw dos atletas que mais maracaram gols durante o período 
campbrasgols["atleta"].value_counts(ascending=False).head(10)
campbrasgols["atleta"].value_counts(ascending=False).head(10).plot.barh()

#Ranking por tipos de gols
campbrasgols["tipo_de_gol"].value_counts(ascending=False)
campbrasgols["tipo_de_gol"].value_counts(ascending=False).plot.barh()

#Quantos cartões foram dados durante todo o período? 
campcart["cartao"].value_counts(ascending=False).head(10)
campcart["cartao"].value_counts(ascending=False).head(10).plot.barh()

#Quantos cartões foram dados relacionando os jogadores que tomaram mais cartões
campcart.groupby(["cartao", "atleta"]).sum().reset_index

#campcart.groupby("cartao").aggregate({"atleta":"sum"})
campcart.groupby(["cartao", "atleta"]).sum()
campcart.groupby(["cartao", "atleta"]).sum().reset_index()
campcart.groupby(["cartao", "atleta"]).sum().reset_index().head(10)

#Relacionar o total de vezes que o atleta recebe o cartao na base de cartões
campcart.groupby("atleta").value_counts()
campcart["atleta"].value_counts(ascending=False)
campcart["atleta"].value_counts(ascending=False).head(5).plot.barh()

#Verificando quantidade de impedimentos ocorridos durante todo o período
campestat["impedimentos"].value_counts(ascending=False)
campestat["impedimentos"].value_counts(ascending=False).plot.barh()
campestat["escanteios"].value_counts(ascending=False).head(5).plot.barh()
campestat["chutes_no_alvo"].value_counts(ascending=False)
campestat["chutes_no_alvo"].value_counts(ascending=False).head(5)
campestat["chutes_no_alvo"].value_counts(ascending=False).head(5).plot.barh()
