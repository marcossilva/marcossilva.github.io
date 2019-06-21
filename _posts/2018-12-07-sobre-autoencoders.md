---
layout: post
title:  "Sobre Autoencoders"
ref: autoencoders
lang: pt
categories: 
tags: redes-neurais python autoencoders keras
---

Já ouviu falar em redes neurais? Eu adoro redes neurais e tem muita coisa para discutir sobre. Hoje eu queria falar um pouco sobre um tipo de rede chamada Autoencoder.

O QUE SÃO AUTOENCODERS?
Autoencoders são um tipo especial de redes neurais que são usados principalmente para comprimir informações com a menor perda possível. Sabe aquele arquivo ZIP ou RAR que você envia por email? Ou aquela imagem JPG que fica pequenininha? Ou ainda quem lembra do MP3? Todos esses são técnicas de compressão de diferentes tipos de arquivo e, por isso, precisam de muito estudo para chegar a técnicas que funcionem bem.

No caso do JPG e do MP3, por exemplo, muito da forma como nós humanos compreendemos e absorvemos esse tipo de mídia é considerado na matemática para compactar esses arquivos. No caso do ZIP e do RAR técnicas mais genéricas são visadas tentando observar organizações inerentes às arquiteturas dos dados e dos hardwares utilizados.
MAS E OS AUTOENCODERS?
Então, os autoencoders são um tipo de rede neural que funcionam como um funil. Autoencoders são compostos de dois blocos: um codificador e um decodificador. No codificador os dados de entrada são comprimidos e n decodificador esses dados comprimidos são descomprimidos.

E POR QUE ISSO É ÚTIL?
Autoencoders são muito úteis para redução de dimensionalidade. Tá, mas o que é isso? Imagina que você tem várias maneiras de representar a mesma coisa mas uma ocupa muito mais espaço que a outra. As vezes queremos guardar só as informações compactas. Isso pode ser percebido em várias técnicas de memorização ou mesmo quando chamamos palha de aço de bombril. 

Autoencoders são usados em:
Técnicas de visualização de dados com muitas dimensões
Compressão de dados
Remoção de ruídos (ou Reconstrução de Dados parcialmente conhecidos)

para quem ficou interessado em saber mais seguem uns links com mais informações de implementações e aplicações
<https://blog.keras.io/building-autoencoders-in-keras.html>
<http://dkopczyk.quantee.co.uk/dae-part1/>

{% include figure.html filename="autoencoders" extension="jpg" alt="Representação de um autoencoder" title="Representação de um autoencoder" caption="Representação de um autoencoder" %}