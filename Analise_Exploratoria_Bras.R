install.packages("dplyr")
install.packages("tidyverse")
install.packages("ggplot2")

library(dplyr)
library(tidyverse)
library(ggplot2)

#Nessa primeira visualização, iremos mostrar a base de cartões
table(campeonato.brasileiro.cartoes$cartao)
  ggplot(data = campeonato.brasileiro.cartoes) +
    geom_bar(mapping = aes(x = cartao))

#Quantos na posição de zagueiro receberam cartão? 
table(campeonato.brasileiro.cartoes$posicao)
  ggplot(data = campeonato.brasileiro.cartoes, stat = "count") +
    geom_bar(mapping = aes(x = posicao))

#Com o objetivo de trabalhar com a base menor, foi realizado o select da base cartões, somente com as variáveis: cartào, clube e atleta  
campeonato.brasileiro.cartoes1 <- select(campeonato.brasileiro.cartoes, cartao, clube, atleta)
  table(campeonato.brasileiro.cartoes1$clube)
    ggplot(data = campeonato.brasileiro.cartoes1, stat = "count") +
      geom_bar(mapping = aes(x = clube)) +
        coord_flip()
    
#Apenas verificando as estatísticas de cada time, iremos para a parte de faltas
table(campeonato.brasileiro.estatisticas.full$faltas)
  campeonato.brasileiro.estatisticas.full1  <- select(campeonato.brasileiro.estatisticas.full, clube, chutes, chutes_no_alvo, impedimentos, escanteios)
    table(campeonato.brasileiro.estatisticas.full1$chutes)
    table(campeonato.brasileiro.estatisticas.full1$chutes_no_alvo)

table(campeonato.brasileiro.full$mandante_Estado)
ggplot(data = campeonato.brasileiro.full) +
  geom_bar(mapping = aes(x = mandante_Estado))
  
table(campeonato.brasileiro.full$visitante_Estado)
ggplot(data = campeonato.brasileiro.full) +
  geom_bar(mapping = aes(x = visitante_Estado))

table(campeonato.brasileiro.gols$tipo_de_gol)
ggplot(data = campeonato.brasileiro.gols) +
  geom_bar(mapping = aes(x = tipo_de_gol))

table(campeonato.brasileiro.gols$atleta)