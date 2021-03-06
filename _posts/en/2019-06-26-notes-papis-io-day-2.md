---
layout: post
title:  "Notes on PAPIs.io (Day 2)"
ref: papis-2
lang: en
categories: en
tags: 
datePublished: 2019-06-26T18:00:00-03:00
dateModified: 2019-06-27T17:52:00-03:00
description: Main topics summary of the watched talks in the second day on presentations in PAPIs.io
image: /assets/papis.png
---

{% include figure.html filename="papis" extension="png" alt="logo of the papis conference" title="PAPIs.io Conference" caption="<a href='https://papis.io'>PAPIs.io</a>"%}

The second day of PAPIs.io was also full of amazing presentations. Among the top knowledges I've gathered from all these talks I can pinpoint:

* There are many iniciatives trying to ease the data science process of data collection, model experimentation, data and model versioning {% include link.html text='1' href='#ludwig-a-code-free-deep-learning-toolbox' target='_self' %} {% include link.html text='2' href='#dataops-architecture-for-machine-learning' target='_self' %}
* There is many initiatives trying to ease the connection between different teams in the data science pipeline. {% include link.html text='2' href='#dataops-architecture-for-machine-learning' target='_self' %} {% include link.html text='3' href='#ai-culture-at-dafiti-and-semi-autonomous-review-approval' target='_self' %}
* There are teams developing solutions focusing to help specifically the data scientist. Those tools are specifically focused on help the programming part of the data scientist. {% include link.html text='1' href='#ludwig-a-code-free-deep-learning-toolbox' target='_self' %} {% include link.html text='4' href='#fklearn-a-functional-library-for-machine-learning' target='_self' %}
* Technical issues in specific models were issued mainly in two talks. 
	* Multitask can be used to solve several problems at the same time helping the model to make quick classification since it shares the convolution layers for different tasks therefore indicating that the convolution really generalized the data. {% include link.html text='5' href='#multitask-convolutional-neural-networks-saving-gpu-time' target='_self' %}
	* Attention models were pointed as a solution to 'embedded' dynamically relational data values into a dense vector to help classifications tasks. {% include link.html text='9' href='#attention-based-neural-networks-for-relational-data' target='_self' %}
* Model interpretability was discussed much more as a reminder that the final user might not fully understand that a model is making decisions and classifications based on its input. The talks mostly pointed that is important to let the final user know which data is being used and how the model ended up getting to that value. {% include link.html text='6' href='#ai-informs-humans-choose----or-do-they' target='_self' %}
* Model validation was treated again in this second day. The validation is first presented as it is treated in academia and taught in the books and then the real world problems are brought upon. It's clear that are many things that must be adapted as no real world set-up can handle AB testing, for example. {% include link.html text='7' href='#validating-models-in-the-real-world' target='_self' %}

## My Watched Talks Index

- {% include link.html text='Ludwig, a Code-Free Deep Learning Toolbox' href='#ludwig-a-code-free-deep-learning-toolbox' target='_self' %}
- {% include link.html text='DataOps architecture for Machine Learning' href='#dataops-architecture-for-machine-learning' target='_self' %}
- {% include link.html text='AI culture at Dafiti and semi-autonomous review approval' href='#ai-culture-at-dafiti-and-semi-autonomous-review-approval' target='_self' %}
- {% include link.html text='FKLearn: A functional library for machine learning' href='#fklearn-a-functional-library-for-machine-learning' target='_self' %}
- {% include link.html text='Multitask convolutional neural networks: saving GPU time' href='#multitask-convolutional-neural-networks-saving-gpu-time' target='_self' %}
- {% include link.html text='AI informs, humans choose -- or do they?' href='#ai-informs-humans-choose----or-do-they' target='_self' %}
- {% include link.html text='Validating models in the real world' href='#validating-models-in-the-real-world' target='_self' %}
	- {% include link.html text='Supervised Learning in ML101' href='#supervised-learning-in-ml101' target='_self' %}
	- {% include link.html text='Supervised Learning in Real World' href='#supervised-learning-in-real-world' target='_self' %}
	- {% include link.html text='Model degradation' href='#model-degradation' target='_self' %}
	- {% include link.html text='Old Policies and bias:' href='#old-policies-and-bias' target='_self' %}
	- {% include link.html text='Engineering' href='#engineering' target='_self' %}
	- {% include link.html text='Business' href='#business' target='_self' %}
- {% include link.html text='Trading strategies using deep reinforcement learning' href='#trading-strategies-using-deep-reinforcement-learning' target='_self' %}
- {% include link.html text='Attention Based Neural Networks for Relational Data' href='#attention-based-neural-networks-for-relational-data' target='_self' %}
- {% include link.html text='Grupo ZAP' href='#grupo-zap' target='_self' %}
- {% include link.html text='Machine Learning for Natural Resources' href='#machine-learning-for-natural-resources' target='_self' %}
- {% include link.html text='Stickers' href='#stickers' target='_self' %}



## Ludwig, a Code-Free Deep Learning Toolbox
**Pierro Molino** - *Sr. Research Scientist, Uber AI*

* Different kinds of data types have different encoding and available decoding.
* With desacoplation of the encoding and decoding in either input and output you can simply re-plug
* The model is mainly defined by hyperparameters in a yaml file and the outputs are text outputs as well which is excellent for model versioning and tracking
* The model is defined as independent DAG which allows an amazing versatility in changing, experimenting and tracking
* All the steps in the process is defined as yaml files, even preprocessing, early stopping, etc.
* Easy to compare models quickly
* Quick to experiment
* The outputs includes: the trained model, visualizations, tensorboard can be used a tracking tool, json output with all the metrics

----


## DataOps architecture for Machine Learning
**Carlos Porto Filho, Gustavo Castilhos** - *Data Scientist, Everis* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/6e/everis_DataOps_Noronha_PAPIs_v1.pptx' text='PDF Presentation' %}
* When a ML project is done? When it reaches 100% acc? When the deadline has passed?
* Why is it so hard to answer that? Business explain the requirements for the DS, the model is developed, but when it is deployed many integrations and iterations are really due to errors


----


## AI culture at Dafiti and semi-autonomous review approval
**Ricardo Savil** - *Data Scientist, Dafiti Group* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/f3/Dafiti%20%40%20papis.io_%20AI%20%26%20case.pdf' text='PDF Presentation' %}

* Ideation -> Detailing (Business Understanding) -> Prioritizing (Score projects and focus on a few) -> PoC (map and experiment)-> Implement (take the experimentation to the main teams) -> Finalization (approval with the business team)


----


## FKLearn: A functional library for machine learning
**Henrique Lopes** - *Machine Learning Engineer, Nubank*

Tutorial on the FKLearn developed by Nubank. Mostly tutorial/quick hands-on. The library has mostly been built on top of other known libraries but focusing on the versatility to call functions and ease the pipeline construction.


----


## Multitask convolutional neural networks: saving GPU time
**Paulo Eduardo Sampaio** - *Data science specialist, McKinsey & Company* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/86/multitask_papis.pdf' text='PDF Presentation' %}
* Single Task Classifier vs Multi Task Classifier
* Single > Input > Conv > Output
* Multi > Input > Conv > [Out1, Out2, Out3, ...]
* Iterator easier than hardcoded becaus it can handle settings like random seed, batch sizes, etc
* The losses can be different so the main loss of the model is the sum of them
* Using the CNN output as embedding and use a single multi-classify output


----


## AI informs, humans choose -- or do they?
**Bianca Ximenes** - *Independent consultant / Doctoral Student, Tecnora / UFPE* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/af/AI%20informs%2C%20humans%20choose.pdf' text='PDF Presentation' %}
* How Google makes trustable models
* {% include link.html href='https://pair.withgoogle.com/' %}
* What is a mental model? 
* The product must ensure that the expectations of the user are aligned with the output of the model
* What is an AI? Is it going to improve? Is the product learning from my feedback?
* Is the user aware of what he can and cannot do with your model? Is it clear in the output?
* Explainability: Why did you output this prediction to this user?


----


## Validating models in the real world
**Luis Moneda** - *Data Scientist, Nubank* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/67/Papis%20-%20Validating%20models%20in%20the%20real%20world.pdf' text='PDF Presentation' %}
### Supervised Learning in ML101

* X -f-> y
* Statistical learning theory
* We want to predict things nicely, we don't care about f
* What do we want? Generalization!
* Training and Validation (Offline) -> Model -> Predictions (Online)
* What validation is about? Asses performance, model selection (validation), generalization power estimation (test)
* Model error mapped as distributions
* Model validation as k-fold
* Split all your data into 3 groups, uses the validation

### Supervised Learning in Real World

* Your x is constantly changing in weird ways
* Random splits imply that future data can be used to predict past
* Temporal split can help mitigate this since it removes this problem
* The validation is probably the data in the nearest future and the test is the data in the far future

### Model degradation
* Complex models degradates over time. More complex models degradates faster.

### Old Policies and bias:
* Models built on top of data that had business rules or other models in the way  is completely biased.
* Conterfactual evaluation: in production disobey your model decision with probability p them you can oversample the unseen classes

### Engineering
How often can I update my model? Is there any time constraint? This influences your timed train-test-validation set split in {% include link.html text='Supervised Learning in Real World' href='#supervised-learning-in-real-world' %}

### Business
Lots of things can change in the X distribution. You can't do but you can monitor the changes to act with policies depending on the impact

{% include link.html href='http://lgmoneda.github.io' %}


-----


## Trading strategies using deep reinforcement learning
**Suraj Shinde, Cristyan Ruffino Gil Morales** - *Director - AI Digital Lab, EVERIS MEXICO S DE RL DE CV, AI Research Lab Leader, everis*

Mainly based on internet tutorials like {% include link.html href='https://www.youtube.com/watch?v=05NqKJ0v7EE' %}

|Market Data -> 			|\|Neural Model | -> Output (Buy, Sell, Hold)
|News Data -> Embedding ->	|\|			  |



----



## Attention Based Neural Networks for Relational Data
**Scott Brownlie** - *Senior Data Scientist, TOTVS Labs* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/1a/Attention-Based%20Neural%20Networks%20for%20Relational%20Data.pptx' text='PDF Presentation' %}
* Attention mechanism assign weights of the historic procedures on the DB
* Based on these weights each data point is consolidated in a single processed data point that is then used to classification
* Compute the scaled dot-produt np.dot(Q, K^T)/sqrt(dim(Q))
* Mask irrelevant weights. In our example we were using 2 patients data. In the matrices multiplication both data were mixed together when actually they don't influence on how the attention should work. Therefore a binary matrix with 1s where the data is passed trough and 0s where is filtered.
* Softmax work as normalizing layer as the sum of all the outputs is 1. The values filtered are then processed as really negative numbers therefore outputing a 0 value in the attention output


-----


## Grupo ZAP
**Lucas Vargas** - *CEO, Grupo ZAP*

Mostly a talk about how ZAP divided São Paulo into blocks that made sense to their business (rental and selling real state). No real technique or algorithm was discussed as the talk was mostly guided by the CEO.


-----


## Machine Learning for Natural Resources
**Bianca Zadrozny** - *Research Manager, IBM*

This talk was mainly the research project listing of IBM in the past few months. But all the projects were presented superficially and didn't seem to have much application in the market. The conclusions were as well partially disappointing as, for example, in one project to detect gold in a given excavation site their model conclusion was that if the initial sample given had gold the probability of gold existing in that cubic meter was high.



----


## Stickers

{% include figure.html filename="paranormal" extension="jpg" width="50%" caption="Paranormal Distribution" %}

{% include figure.html filename="orgulho" extension="jpg" width="50%" caption="Orgulho LGBT+" %}

{% include figure.html filename="data_is_the_new_bacon" extension="jpg" width="50%" caption="Data is the new Bacon" %}

{% include figure.html filename="random_forests" extension="jpg" width="50%" caption="I camp in Random Forests" %}

{% include figure.html filename="email_atitude" extension="jpg" width="50%" caption="Less Email More Attitude"%}

{% include figure.html filename="pandas_play" extension="jpg" width="50%" caption="I play with pandas" %}

{% include figure.html filename="problem_solution" extension="jpg" width="50%" caption="Don't point the problem, find the solution" %}