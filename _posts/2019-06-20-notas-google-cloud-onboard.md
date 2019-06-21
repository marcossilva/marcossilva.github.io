---
layout: post
title:  "Notas do Google Cloud OnBoard"
ref: google-cloud-onboard
lang: pt
categories: 
tags: google-cloud negocio
datePublished: 2019-06-20T16:00:00-03:00
dateModified: 2019-06-20T17:52:00-03:00
description: Nesse post eu descrevo os tópicos principais que anotei durante a aprensetação do Google Cloud OnBoard
image: /assets/google-cloud.jpg
---
<figure>
	<p align="center">
		<picture align="center">
		  <source srcset="/assets/google-cloud.webp" type="image/webp">
		  <source srcset="/assets/google-cloud.jpg" type="image/jpeg"> 
		  <img src="/assets/google-cloud.jpg" title="Google Cloud Logo" alt="logo nuvem do google cloud">
		</picture>
	</p>
	<p align="center"><figcaption align="center">GCP - Muitas oportunidades dentro de uma só plataforma</figcaption></p>
</figure>

Participei remotamente nessa última 3a (18/06/2019) da apresentação do Google OnBoard e fiz várias anotações por alto das inúmeras demonstrações e do enorme potencial que as ferramentas do Google podem ajudar a trazer para o negócio. Abaixo eu comento cronológicamente os tópicos que foram discutidos no evento e pontuo aqui e ali os respectivos momentos do talk no <a href='https://youtu.be/26Dewxxq1-0' rel='nofollow'>vídeo disponível no youtube.</a>Esse foi a 2a parte do evento mais focada na parte técnica de ferramental, Machine Learning e AI que é exatamente a parte que eu tenho maior interesse.

* **Estabilização de Vídeo**: Massa de dados diária (PB) -> Treinamento na plataforma -> Deploy do modelo treinado servido no aplicativo

* Limite físico das unidades de processamento -> Criação de unidades específicas para utilização em ML (TPU)

* Aplicação de ML interna permite otimizações físicas nos próprios DataCenters da empresa (ar-condicionado)

* VM:
	* Como criar?
	* Onde criar?
	* Qual a capacidade de processamento que eu preciso?
	* Qual a memória necessária para o meu projeto?

* **Organização de Bucket**: Bucket -> Pasta -> Projeto -> Recurso

* Buckets:
	* Como criar?
	* Onde alocar?
	* Qual tipo de acesso?
		A partir de diferentes tipos de acesso faz sentido configurar diferentes buckets com diferentes latências e responsabilidades. Buckets podem ser locais, multi-região, de armazenamento (e acesso) mensal, como backups, ou de recuperação de catrástrofes, com acesso anual

* As atividades a serem computadas fazem sentido serem executadas no mesmo local onde estão armazenadas por simples motivo de acesso. Moviemntações constantes de dados através da rede gastam banda que são custosos para a rede e também para o usuário.

* VPC:
	* Regras de Firewall: TODAS as portas bloqueadas por default
	* Inclusive 22 (SSH) e ping
	* Permite criar uma rede de baixa latência entre máquinas em diferentes locais

* Papers das ferramentas disponíveis em :<http://research.google.com/pubs/papers.html> (OLD) -> <https://ai.google/research/pubs> (NEW)

* Onde buscar referências? Quais serviços usar pra quais fins?

* Casos de Uso: 
	* AutoML Vision usado para reconhecer características de imagens de imóveis para aluguel de modo a extrair features do imóvel a ser alugado e permitir a filtragem automática
	* AutoML NLP usado para triagem específica de problemas
	* KewPie usando Visão copmutacional para avaliar qualidade do processo de seleção de comidas

* Go-JEK moveu seus dados para o GCP de modo a gerenciar suas análises para tempo real e não mais D+1. Através da coleta pelo pub/sub e análise com a arquitetura abaixo foi possível gerenciar em tempo real 


## Módulo 2: Recomendação com Spark e SparkML

* E-commerce com recomendação de produtos
* Google Smart Reply do GMail
* Google Photos com agrupamentos de imagens
* Google Maps com sugestão de restaurantes que você pode gostar

* **PROBLEMA**: como capturar de maneira escalável e treinar esses modelos?

* Modelo antigo: Regras fixas
* Modelo de dados: Exemplos baseados nos dados
* Machine Learning = Exemplos, não regras

* Com que frequência eu re-treino? Streaming ou Lote?
* No caso de e-commerce não há necessidade de negócio de responder em tempo real para retreino do modelo. Nesse cenário o Hadoop é uma opção.
* Antigamente era necessário extrair os dados e fazer o processamento posterior. Com o surgimento do Hadoop em 2006 tornou-se mais simples deixar o processamento distribuído próximo aos dados. Com a evolução dos serviços pra nuvem o GCP configurou esses serviços a serem portados pra nuvem de modo a adicionar ainda escalabilidade a eles.
*  Datacenter on-premise:
	* Cenário 1: Muitos jobs competindo por recurso e tarefas com atividades maiores ganham prioridade
	* Cenrário 2: Poucos jobs com recurso sobrando -> Gastos desnecessários
	* Cenário Recomenado: Criação do Cluster por Job permitindo subir cluster de alta resposta e capacidade de processamento em paralelo
* Desacople o armazenamento do processamento

## Dados:
* Cloud SQL: MySQL no Google
	* Todo o processo de armazenamento e gerência é papel do Google
* BigQuery: (Analytics Engine)
	1. Sistema Serverless de DataWarehouse. Query SQL
	2. Modelo de preço flexível
	3. Criptografia de Dados e segurança
	4. Funções de dados espaciais
	5. ML e IA

> "É muito fácil extrair conhecimento de dados organizados"


## Machine Learning com BigQuery


A equipe do Google implementou uma maneira simples e direta de poder treinar modelos diretamente no BigQuery e avaliar todas as métricas competentes aos modelos respectivos. Durante a apresentação eles apresentaram alguns exemplos ótimos de maneira rápida, como pode ser visto a partir daqui, mas se você quer mais do que só um exemplo a documentação está disponível [aqui](https://cloud.google.com/bigquery-ml/docs/bigqueryml-intro)

## Dashboard em tempo real

* Arquitetura orientadas a mensagens
* Pub/Sub -> Publisher/Subscriber

### Pub/Sub Demo
* Criar um tópico
* Criar um assinante desse tópico
* Postar mensagem nesse tópico

## Encerramento com a Palestra da <a href='https://www.linkedin.com/in/tmnakano/' rel='nofollow'>Talita Nakano</a>

O evento teve muitos desafios técnicos para mostrar todo potencial e todas as funcionalidades que a plataforma do GCP já oferece e passa a oferecer incrementos todo dia. Tendo em vista tudo isso o evento acabou demorando mais para acabar do que o planejado e muitos acabram saindo antes do fim. Eu acabei ficando até o final e assisti o <a href='https://youtu.be/26Dewxxq1-0?t=16799' rel='nofollow'>pitch da Talita Nakano</a>. Ela contou a trajetória de migração dela pra uma vaga de TI, todo o árduo processo de contínuo aprendizado e todo o suporte que ela conseguiu de contatos. Comentou como é importante sabermos criticar quanto nós **não sabemos** de modo que sejamos capazes de correr atrás e nos informar.

Networking também foi um tópico comentado no pitch dela pois foi uma das estratégias que ela usou pra tentar se aprofundar nessa nova área pra ela. Concordei fortemente com ela no momento que ela apontou que a área de negócio está muitas vezes muito distante da área de TI e que isso acaba prejudicando ambos. Têm sido cada vez mais importante o papel de intermediário entre esses dois campos. 

Achei muito legal que ela comentou também que quando entrou no Google os profissionais são estimulados a errar, são colocados sempre fora da sua zona de conforto. Eu acho isso muito importante pois só assim os profissionais conseguem desenvolver suas habilidades em profundidade com alguma noção de como isso se conecta com as outras áreas em largura. É muito incômodo pra muitos estar sendo desafiado o tempo todo mas é o que acaba impulsionando muito o rápido crescimento profissional. 

Ela comentou então da importância que está sendo capacitar profissionais nas ferramentas que eles oferecem rapidamente uma vez que a demanda é tão alta e a quantidade de profissionais qualificados é tão escassa. Ela comentou então das trilhas de curso disponíveis no Coursera onde o Google oferece certificação e apontou as trilhas base para alguns tipos de profissionais.

> O sucesso é a soma de pequenos esforços repetidos dia a dia

> A força não provém da capacidade física, ela provém da nossa capacidade indomável. (Gandhi)

## Comentários Finais

Das inúmeras demonstrações pontuadas por comentários cômicos de funcionar na demo ficou claro que é um desafio para todos de TI (mesmo para o time do Google) conectar todas as ferramentas. Isso é muito legal pois me estimula a acreditar que esses desafios são comuns a todos os profissionais da área. Como a Talita comentou fortemente na palestra dela profissionais qualificados estão escassos e o Google está tomando frente nos dois melhores caminhos, na minha opinião, pra suprimir essa falta: oferencendo sempre ferramentas mais simples, poderosas e funcionais em paralelo a uma oportunidade constante de aprendizado reconhecido com certificações. Espero conseguir em breve minhas certificações assim como colocar em prática todo material que possa agregar valor para o meu time  :)