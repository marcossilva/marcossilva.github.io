---
layout: post
title:  Quais cursos devo fazer para começar em Data Science?
ref: cursos-ds
lang: pt
categories: 
tags: cursos
datePublished: 2019-09-15T19:33:00-03:00
dateModified: 2019-09-15T19:33:00-03:00
description: Muitos amigos e pessoas vem me perguntar o que devem estudar para entrar na área de Data Science e eu acabo dando orientações personalizadas baseadas no que eu conheço das pessoas. Mas minhas orientações seguem uma receita de bolo com algumas fontes e alguns conteúdos que sempre se repetem. Aqui resumi alguns conteúdos que podem ser úteis para várias pessoas.

---

Muitos amigos e pessoas vem me perguntar o que devem estudar para entrar na área de Data Science e eu acabo dando orientações personalizadas baseadas no que eu conheço das pessoas. Mas minhas orientações seguem uma receita de bolo com algumas fontes e alguns conteúdos que sempre se repetem. Eu acredito que essa é uma área que as pessoas devem estar sempre procurando estudar e se atualizar se querem mesmo saber do que está acontecendo. Por isso acredito que qualquer guideline é apenas um esboço inicial e introdutório do mínimo necessário para o assunto. Acredito que é responsabilidade da pessoa que está estudando decidir suas trilhas e seus objetivos antes de sair estudando. Existe muito material na internet e isso pode ser estarrecedor para muitos. Eu também não acredito em cursos que se propõe a ensinar todos os assuntos em um período muito reduzido de tempo, acho que são apenas armadilhas para os desavisados por isso evito recomendar esse tipo de conteúdo também. Se você nem sabe o que é Machine Learning dá uma olhada nessa {% include link.html href="https://cloud.google.com/products/ai/ml-comic-1/" text="tirinha do Google"%} pra entender.

## Desenhando seu perfil

### Quem sou eu e onde quero chegar?

Para começar acho você que está começando na área desenhar o seu perfil atual e onde você quer chegar. A área de dados é muito grande e possivelmente não há como se tornar especialista em todas as frentes sem nenhum background. Recentemente no Linkedin vi a imagem abaixo e acho um bom indicador dos perfis gerais que conheço da área:


{% include figure.html filename="radial_diagram" extension="png" caption="Conhecimentos dos Principais Perfis da Área" alt="perfis de um data scientist, um data engineer e um data analyst" %}

Eu acho essa imagem boa pois ela deixa claro alguns fatores que muitas pessoas que entram na área tem dificuldade de entender:
* Diferentes perfis ainda possuem uma grande intercessão. Mesmo que os pontos fortes de especialização sejam diferentes existe muita coisa em comum entre eles
* Uma pessoa que está entrando na área possivelmente vai estar com uma pontuação baixa em todos as direções. Mas já que a intercessão das áreas é tão grande é uma excelente oportunidade pra se aprender de tudo um pouco e tentar decidir qual o melhor perfil se adéqua para si

### Mas existem muitas especializações nessa área

Além desses perfis mais conhecidos e genéricos dispostos no gráfico acima podemos ver abaixo outra possível separação de profissionais da área:

{% include figure.html filename="careers_ds" extension="jpeg" caption="Conhecimentos dos Principais Perfis da Área" alt="perfis de um data scientist, um data engineer e um data analyst" %}

Nessa imagem agora conseguimos entender que diferentes profissionais de outras áreas já possuíam backgrounds que os colocavam com alguma expertise num determinado assunto. Mas não é incomum ver uma deficiência em algum outro aspecto conforme o gráfico de radar de antes.

Para mim é claro que a base dessa área como um todo é um conhecimento mínimo de matemática e estatística. Além disso eu acho essencial também que o profissional desenvolva conhecimento em alguma linguagem de programação. Existem soluções prontas como o SAS ou o Excel mas isso faz com que as pessoas fiquem presas. O profissional que só usa Excel acaba escravo das planilhas, muitas vezes não entende o que está sendo calculado ali e isso pode levar a erros catastróficos, por exemplo {% include link.html href="https://www.sciencemag.org/news/2016/08/one-five-genetics-papers-contains-errors-thanks-microsoft-excel" title="One in five genetics papers contains errors thanks to Microsoft Excel" text="erros em publicações científicas"%}. 

Eu uso **python** como linguagem de programação pela flexibilidade que ela me dá em lidar com todo tipo de solução para o pipeline de dados (como coleta de dados com scrapping ou subir uma aplicação em produção serverless com um código python). R e Julia são opções relativamente famosas mas desconheço facilidades comparativas para estender seu uso para além da análise.

{% include figure.html filename="spreadsheets" extension="png" caption="As desvantagens e limitações de usar o Excel" %}

### Beleza. Entendi que tem muito que estudar. Por onde eu estudo?

Na internet existem muitas fontes boas para se estudar todos os assuntos na área de dados. Antes de falar delas queria trazer a tona dois pontos fortes: a vantagem de falar inglês e a as várias armadilhas para enganar os desavisados.

#### Das vantagens de falar inglês

Não vou me estender tanto aqui mas só queria reforçar que quem tem o domínio da língua inglesa tem uma vantagem no quesito de ter uma quantidade muito maior de material pra consumir. Existem materiais em inglês e existe uma comunidade enorme que dá suporte. Mas quando o assunto é volume tanto a quantidade de material quanto o número de pessoas disponíveis pra discutir em inglês acaba sendo muito maior. Eu acho que pra área de TI como um todo é um diferencial ter conhecimento da língua.

#### Das armadilhas, dos salafrários e outros

Como eu disse tem MUITO material na internet mas acontecem duas coisas com esse material todo:

1. Muito dele está desorganizado, o que atrapalha muito quem está entrando na área
2. Muito dele está em inglês, que é o que eu acabei de falar

Daí o que tem acontecido é cursos se estruturarem em cima de materiais que não são deles apenas organizando materiais gratuitos da internet ou mesmo traduzindo-os e cobrando taxas enormes como se tivessem realmente produzido o material. Isso tem gerado uma discussão e um desconforto enorme na comunidade. Eu entendo a sede de quem está entrando na área ver um curso de 12 semanas e achar que sairá com domínio total dos assuntos. Eu acho improvável e não recomendo. Existem vários estudos que apontam como o conhecimento precisa ser absorvido aos poucos pelo cérebro e reutilizado de tempos em tempos (tipo como usam na {% include link.html href="https://www.youtube.com/watch?v=CN_SCpGuJ_w" title="Como APRENDER QUALQUER COISA de maneira INTELIGENTE | A Técnica Feynman" text="técnica de feynman"%} ou como discutem a {% include link.html href="https://www.youtube.com/watch?v=xg41NyKFK24" title="Como tornar-se um MESTRE em QUALQUER COISA | MAESTRIA | George Leonard | Resumo Animado" text="regra das 10.000 horas"%} )

## Fontes de estudo

Para aprender algo na área eu uso muito conteúdos escritos (livros e sites) e conteúdo visual (vídeos, palestras e aulas). Livros são os mais propensos a ficarem desatualizados pela própria natureza do material mas quando o assunto é bem embasado na área (matemática, estatística, algoritmos, etc) costumam ser excelentes referências por anos. Uma dica que eu acho boa seguir pra qualquer conteúdo a se ingerir é só levá-lo até o ponto que faz sentido. Se eu quiser um insight de como representar uma informação num gráfico vou consultar minha literatura de visualização de dados pertinente ao que quero representar. 

### Coursera - 7 day trial e Modo Ouvinte
O Coursera é uma das minhas plataformas favoritas pra aprender. Eles tem um bom aplicativo de celular e em muitas faculdades renomadas com cursos em seu portifólio. Alguns cursos inteiros estão disponíveis pela plataforma mas atualmente o coursera tem um módulo de sugerir que você se inscreva no curso como aluno pagante. O que eu prefiro fazer é assistir as aulas primeiro como aluno ouvinte, fazer todos os exercícios e quizzes e guardar minhas respostas. Daí quando acabo todos os cursos de uma especialização solicito o trial, submeto minhas respostas e pego os diplomas.

### Certificações e Diplomas vs Portifólio

Infelizmente o mercado precisa de uma maneira para validar que você tem um certo conhecimento no assunto. A maneira clássica de fazer isso era pedindo certificados e diplomas. Muitas empresas ainda pedem apenas funcionários com nível superior mas eu discordo dessa abordagem. Acredito que com todo o material disponível todos tem igual potencial de aprender e agregar valor. Mas enquanto isso uma solução é continuar fazendo cursos pelos certificados. 

Uma solução presencial é fazer um mestrado ou MBA na área. Mas essas opções demandam tempo, dinheiro e flexibilidade do empregador. Nem sempre esses três tópicos conversam bem. Além disso eu percebi uma euforia dos cursos em criar cursos com "data science" no nome apenas para atrair alunos então se o intuito é aprender apenas eu evitaria (ou daria menor importância) nessa rota.

Outra solução para se posicionar na área é montar um portifólio com os projetos que você for desenvolvendo ao longo dos cursos que for fazendo. Quanto mais fácil for pra explicar e vender o projeto melhor. Um diferencial também é ser criativo e fazer seus próprios projetos, não apenas copiar tutoriais e soluções que já foram apresentadas inúmeras vezes.

### Cursos introdutórios e de matemática

O {% include link.html href="https://pt.khanacademy.org/" title="Khan Academy | Cursos, aulas e prática on-line gratuitos" text="Khan Academy"%}  tem um excelente material pra quem precisa revisar a **matemática**, a **álgebra linear** e a **estatística**. Stanford também oferece na plataforma deles cursos de {% include link.html href="https://lagunita.stanford.edu/courses/HumanitiesSciences/StatLearning/Winter2016/about" title="Statistical Learning" text="estatística"%} estatística com certificação.


No Coursera o {% include link.html href="https://www.coursera.org/specializations/mathematics-machine-learning" title="Mathematics for Machine Learning Specialization" text="Mathematics for Machine Learning Specialization"%}, o {% include link.html href="https://www.coursera.org/professional-certificates/ibm-data-science" title="IBM Data Science Professional Certificate" text="IBM Data Science Professional Certificate"%} e o {% include link.html href="https://www.coursera.org/specializations/jhu-data-science" title="Data Science Specialization by Johns Hopkins University" text="Data Science Specialization by Johns Hopkins University"%} são cursos que cobrem bem os tópicos básicos de **análise de dados**, **programação em python**, **visualização de dados** e **modelos simples de machine learning**.


No YouTube o canal do {% include link.html href="https://www.youtube.com/user/joshstarmer" title="StatQuest with Josh Starmer" text="StatQuest with Josh Starmer"%} é uma excelente fonte para todos os tópicos pois ele trata dos assuntos de maneira modular e com dicas visuais que só facilitam a compreensão. Ele também tem playlists para cada assunto (tópicos básicos e machine learning). O canal do {% include link.html href="https://www.youtube.com/user/marionefilho" title="Mario Filho" text="Mario Filho"%} é uma boa fonte pra quem prefere consumir conteúdo em português. O EstaTiDados organizou recentemente uma {% include link.html href="https://www.youtube.com/playlist?list=PLjdDBZW3EmXe6hO2Rt5Q9I5wzRZ7j7K8P" title="Trilha EstaTiDados – Data Science" text="playlist de Data Science"%}.

O **Kaggle** é uma plataforma de competição de dados também oferece vários cursos introdutórios na área disponíveis {% include link.html href="https://www.kaggle.com/learn/overview" title="Faster Data Science Education" text="aqui"%}. São micro-cursos que não tem certificação mas tratam rapidamente de tópicos necessários para qualquer data scientist da aŕea.

Uma das bibliotecas mais básicas que eu acho que todo Data scientist deve saber é o **pandas**, que é uma biblioteca do python. O curso do Kaggle é uma boa referência pra quem nunca viu mas também a {% include link.html href="https://pandas.pydata.org/pandas-docs/stable/index.html" title="pandas: powerful Python data analysis toolkit" text="documentação da biblioteca"%} e uma maneira diferente de fazer um código {% include link.html href="https://realpython.com/fast-flexible-pandas/" title="Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects" text="efetivamente flexível e rápido"%}


### Cursos intermediários
Para quem só quer entender como aplicar o modelo de dados no negócio o livro "Machine Learning Yearning" do Andrew Ng é uma boa. É um livro curto e direto que facilita a vida de pessoas que lidam mais com o negócio e precisam tomar decisões orientadas a dados.

Com um background mínimo de matemática o livro "Learning From Data" do Yaser S. Abu-Mostafa, Malik Magdon-Ismail, Hsuan-Tien Lin assim como o "Pattern Recognition and Machine Learning" do Christopher M. Bishop são excelentes fontes teóricas de todas as definições importantes que fundamentam a área de análise de dados e machine learning.

No Coursera um dos cursos mais antigos e populares da plataforma é o de {% include link.html href="https://www.coursera.org/learn/machine-learning" title="Machine Learning" text="Machine Learning pelo Andrew Ng"%}. O curso data de 2012 e, na época, Andrew decidiu lecionar o curso usando Octave (um primo open-source do Matlab). O intuito de decidir por essa ferramenta era implementar todos os algoritmos manualmente. Atualmente já implementaram os correspondentes para linguagens mais populares e acredito que possa ser benéfico acompanhar o curso paralelamente em mais de uma linguagem.

Outro curso bom é o {% include link.html href="https://www.coursera.org/specializations/data-science-python" title="Applied Data Science with Python Specialization" text="Applied Data Science with Python Specialization"%} que tem um escopo mais amplo que o curso do Andrew mas mais superficial no aspecto matemático.

### Cursos avançados
Como meu interesse maior é em machine learning e deep learning os tópicos que eu considero avançados são mais focados nessa área. Existem tópicos avançados a serem discutidos em todas as áreas (engenharia de dados, compreensão do negócio, visualização de resultados, etc) mas para esses acho que existem guidelines melhores nos "Outros Cursos" a seguir.

#### Deep Learning
O livro mais famoso da área é o "Deep Learning" por Ian Goodfellow, Yoshua Bengio, Aaron Courville. O livro tem um foco mais teórico onde explica detalhadamente a parte mais matemática por detrás dos modelos.

No Coursera, novamente com o Andrew NG, temos o {% include link.html href="https://www.coursera.org/specializations/deep-learning" title="Deep Learning Specialization" text="Deep Learning Specialization"%}. O curso foi lançado em 2015 e explica muito bem toda a base de redes neurais, a estruturação de projetos de machine learning e utilizações mais populares dos modelos até a época. Devido ao rápido desenvolvimento da área acredito que ele seja muito bom mas precisa de material extra para acompanhar os algoritmos que são estado da arte atualmente. O Curso {% include link.html href="https://onlinehub.stanford.edu/cs230" title="CS230: DEEP LEARNING" text="CS230: DEEP LEARNING"%} oferecido por Stanford e também lecionado pelo Andrew Ng é um bom complemento de atualidades que estão defasadas da especialização do Coursera. Mas nesse curso é necessário fazer a especialização em paralelo para conseguir acompanhar.

Outro especialização boa no Coursera é {% include link.html href="https://www.coursera.org/specializations/aml" title="Advanced Machine Learning Specialization" text="Advanced Machine Learning Specialization"%} que lida com todos os tópicos principais de modelagem de modelos, deploy na nuvem e avaliação dos modelos.

Um curso que se propõe a ser mais rápido para quem tem um background de desenvolvimento é o {% include link.html href="https://course.fast.ai/" title="Practical Deep Learning for Coders" text="Practical Deep Learning for Coders"%} que está atualmente na sua 3a versão. O curso preza muito mais pela aplicabilidade rápida e execução do que de fato explicar com detalhes minuciosos tudo que acontece. Mas é um curso que também trata de tópicos únicos raramente discutidos em outras frentes então tem seu valor.

Particularmente para **NLP** e **modelos sequenciais** existe o curso de Stanford que está disponível no YouTube nas aulas de {% include link.html href="https://www.youtube.com/watch?v=OQQ-W_63UgQ&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6" title="Natural Language Processing with Deep Learning" text="2017"%} e {% include link.html href="https://www.youtube.com/watch?v=8rXD5-xhemo&list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z" title="Stanford CS224N: NLP with Deep Learning | Winter 2019" text="2019"%}. O material também está disponível no {% include link.html href="https://onlinehub.stanford.edu/" title="STANFORD CENTER FOR PROFESSIONAL DEVELOPMENT AI RESOURCE HUB" text="site"%} com links para os PDFs das aulas e os devidos exercícios dos cursos abertos. 

No Youtube existem {% include link.html href="https://www.youtube.com/channel/UCcQgGC19k35ayQNsspyyBhQ" title="School of AI São Paulo" text="School of AI São Paulo"%} e {% include link.html href="https://www.youtube.com/channel/UCZ8gRCp3vixlGVAtplCDd5Q" title="Minerando Dados" text="Minerando Dados"%}

### Outros cursos/outras fontes

O Coursera tem várias outras {% include link.html href="https://github.com/ossu/data-science" text="trilhas de Data Science"%}. O Google também tem seu próprio {% include link.html href="https://developers.google.com/machine-learning/" title="Machine Learning Crash Course" text="curso rápido de Machine Learning"%}. Como é um curso rápido ele assume que você já tem domínio de vários assuntos e passa bem rápido pelos assuntos.

Alguns youtubers publicam vários vídeos relacionados no tema de data science mas nem sempre são focados em ensinar. Abaixo tem alguns canais que eu sigo e acho legal compartilhar:

* <https://www.youtube.com/user/sentdex>
* <https://www.youtube.com/channel/UCV0qA-eDDICsRR9rPcnG7tw>
* <https://www.youtube.com/channel/UCr8O8l5cCX85Oem1d18EezQ>
* <https://www.youtube.com/user/sethbling>

Tem dois canais no Youtube de Streamings de palestras que tem conteúdos de todos os níveis. O primeiro é o pyData que acontece em vários lugares do mundo (inglês) e o segundo é o Meetup do Nubank (português).

* <https://www.youtube.com/user/PyDataTV>
* <https://www.youtube.com/channel/UC5yS6v2umoIXx8TSJsUEBKg/videos>

Além disso tudo redes sociais são uma boa fonte de se manter por dentro dos trending topics. Para isso eu uso o Twitter e o Reddit. Seguem abaixo minhas listas de conteúdo que contém vários canais que você pode seguir:

* <https://www.reddit.com/user/marcossilva_604/m/ml/>
* <https://twitter.com/marcospedro/lists/machine-learning-ds>

Alguns livros que acho válidos recomendas também são:

sobre data science:
* The Data Science Handbook
* The Data Science Manual - Steven Skiena


sobre visualização de dados:
* Data Visualization Made Simple - Insights into Becoming Visual por Kristen Sosulski
* Storytelling with Data - Cole Knaflic
* The truthful art - Alberto Cairo

Um livro que não é exatamente sobre estatística mas sim sobre como as pessoas ingerem resultados e como é importante ter sempre um senso crítico é o Como Mentir com Estatísticas do Darrel Huff. Esse é um livro já bem antigo mas os exemplos permanecem válidos. Muitos resultados exibidos hoje em dia tem problemas na apresentação no ponto de querer 

Por fim estudar e tirar dúvidas junto com a comunidade ajuda. Existe um grupo no Telegram (@datasciencepython) muito bom. Caso queira entrar em contato minhas redes sociais estão no rodapé da página. Espero que essa extensa lista de cursos e opiniões/dicas seja uma referência para iniciar/continuar seu aprendizado. 