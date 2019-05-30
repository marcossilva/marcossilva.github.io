---
layout: post
title:  "A mágica dos Modelos Recorrentes Baseados em Caracteres"
ref: rnn-char-level
lang: pt
categories: 
tags: python nlp texto redes-neurais distancia
---


Recentemente eu estava fazendo um trabalho onde precsava classificar diversos produtos em suas devidas categorias a partir dos seus títulos. Isso parece relativamente fácil mas existiam dois grandes problemas: haviam cerca de 18 milhões de produtos no catálogo e eu não tinha certeza que eles haviam sido cadastrados corretamente nos departamentos correspondentes. Esse é um cenário comum no cotidiano de dados em larga escala e eu tinha que propor uma solução.

## 1a Abordagem: Modelos Clássicos
Uma primeira soluçao foi montar um classificador a partir desses dados mas sem esperar altas acurácias. Um dos grandes problemas em trabalhar com texto é a falta de estruturação dos dados. Claro que existem técnicas como CountVectorizer, TF-IDF . Tendo em vista a grande quantidade de produtos eu era incapaz de cortar palavras que aparecessem com uma frequência muito baixa pois esses seriam ótimos indicadores de produtos raros. Cortar termos com frequência muito alta (stop words) também é ruim pois ocasionalmente determinam modelos (e.g. Moto E).

De cara as vetorizações clássicas já eram problemáticas. Aplicando ambas nos meus dados obtive vetores de ~500k features. Tentei ainda cortar valores numéricos ou reduzir a dimensionalidade desse vetor com um Autoencoder mas não tive bons resultados. Independente do modelo que eu usasse para classificar esses vetores os resultados eram ruins então parti para a 2a abordagem.

## 2a Abordagem: Modelos Neurais
### Palavras como Tokens
Eu já conhecia alguns modelos neurais para problemas de NLP famosos como o word2vec. Nesse modelo uma rede neural aprende uma representação densa para as palavras a partir de suas palavras vizinhas. É uma estratégia interessante pois acaba capturando bastante a semântica do texto. Ainda temos ~500k termos únicos mas que podem ser comprimidos num vetor de representação densa do tamanho desejado. Tomando essa estratégia como vetorizador e uma rede de convoluções 1D para funcionar como n-grams fomos capazes de obter bons resultados. O problema no nosso caso é que o texto do título de produtos costuma ser curto e por isso não tem semântica. Daí muitas vezes a representação densa da palavra não era bem aprendida e o modelo era incapaz de classificar corretamente.

### Caracteres como Tokens
Uma outra alternativa possível foi ao invés de se usar a palavra inteira como token usar caracteres. Pode parecer estranho dado que o princípio da técnica original era capturar semântica. Mas pense nesse modelo como um jogo da forca de uma frase qualquer. Você tem acesso às letras próximas mas não sabe ainda qual é a letra onde está. Na imagem abaixo podemos ver um jogo da forca com a palavra livraria. Então se o modelo usasse apenas as letras vizinhas deveria tentar prever o ‘i’ faltante da 2a posição a partir das letras ‘l’ e ‘v’.

<figure>
	<p align="center"><img src="/assets/hangman.png" title="Jogo da Forca" alt="Jogo da Forca" align="center"></p>
	<p align="center"><figcaption align="center">Jogo da Forca</figcaption></p>
</figure>

Daí temos um cenário mais promissor na quantidade de tokens: caímos de ~500k palavras únicas para ~200 caracteres únicos (contando caracteres acentuado, especiais, números, etc). Isso facilita muito o modelo a criar representações boas para as letras mesmo usando as mesmas técnicas de convolução 1D do modelo anterior. Nesse cenário a convolução 1D representaria o tamanho da janela lateral responsável por ajudar a prever a letra faltante. Esse modelo superou todos os anteriores em performance, velocidade de treino e acurácia na resposta final.

## Conclusão
Como resultado temos que modelos neurais são ótimos para capturar representações dos próprios dados quando eles existem. Entretanto no nosso cenário não existia muita semântica entre os termos de título de produto e por isso o modelo por palavras não funcionou tão bem. Talvez esse modelo pudesse ser melhr aplicado às descrições e não aos títulos. Por sua vez os modelos de caracteres sempre performam bem e de maneira genérica pois também possuem uma interpretação própria e uma dimensão compacta.