---
layout: post
title:  Qual a diferença de src e href nas tags HTML?
ref: title-tag
lang: pt
categories: 
tags: seo
datePublished: 2019-07-19T19:36:00-03:00
dateModified: 2019-07-19T19:36:00-03:00
description: src e href podem ser enontradas em outras tags. O conceito geral é que utiliza-se src quando queremos carregar e inserir o conteúdo do link naquele local da página e o href quando queremos esperar uma interação do usuário para carregar o conteúdo.
---

## Cara de uma tag *img* (imagem)
Uma tag de imagem em HTML tem a seguinte cara
```HTML
<img src="smiley.gif" alt="Smiley face">
```
Onde *<img>* determina que é uma tag de imagem, *alt* determina o texto alternativo caso a imagem não carregue ou para aumentar a acessibilidade do texto e por fim o *src* que aponta para o endereço da imagem

## Cara de uma tag *a* (link)
Uma tag de imagem em HTML tem a seguinte cara
```HTML
<a href="https://www.americanas.com.br">Link par Americanas.com</a>
```
Onde *<a>* determina a abertura da tag de link, sendo fechada pela referente *</a>*; O texto entre a abertura e o fechamento da tag, *Americanas.com* e por fim o *href* que aponta para o endereço que o link direciona.

## Beleza. Mas qual a diferença?

*src* e *href* podem ser enontradas em outras tags. O conceito geral é que utiliza-se *src* quando queremos carregar e inserir o conteúdo do link naquele local da página e o *href* quando queremos esperar uma interação do usuário para carregar o conteúdo.

No caso da imagem queremos que a imagem carregue ali, naquele local da página. Enquanto no exemplo da tag a não queremos que nenhum conteúdo seja de fato renderizado automaticamente, queremos apenas permitir que o link aponte o usuário para outra página, apenas gerando resultados após uma interação com o usuário.

## E quem definiu isso??

A internet. Quando começaram a pensar na internet lá em 1993 o pessoal já estava discutindo sobre isso numa enorme thread de emails <http://1997.webhistory.org/www.lists/www-talk.1993q1/0188.html>. Em algum momento até chegaram a pensar em usar uma propriedade só e indicar quando o conteúdo deveria carregar e quando não devia. Mas por isso ser tão verboso acabaram implementando da maneira atual.

## Pera mas eu uso *href* quando uso pra inserir meu CSS com a tag *link*. Por que é assim?

A

Existe essa exceção. 🤷

Ela é fruto da documentação do HTTP/2 <https://www.ietf.org/rfc/rfc1866.txt> e até hoje gera confusão de vez em quando. Como essa tag aparece (usualmente) no head da página acaba sendo carregado automaticamente mesmo usando href (além do comportamento pro CSS ser inconsistente as vezes em relação aos outros conteúdos).

