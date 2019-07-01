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
<div style="background-color: black;">
<a href='https://papis.io'>
{% include figure.html filename="papis" extension="png" alt="logo of the papis conference" title="PAPIs.io Conference" caption="PAPIs.io"%}</a></div>

The second day of PAPIs.io was also full of amazing presentations. Among the top knowledges I've gathered from all these talks I can pinpoint:

* There are many iniciatives trying to ease the data science process of data collection, model experimentation, data and model versioning [\[1\]](#ludwig-a-code-free-deep-learning-toolbox) [\[2\]](#dataops-architecture-for-machine-learning)
* There is many initiatives trying to ease the connection between different teams in the data science pipeline. [\[2\]](#dataops-architecture-for-machine-learning) [\[3\]](#ai-culture-at-dafiti-and-semi-autonomous-review-approval)
* There are teams developing solutions focusing to help specifically the data scientist. Those tools are specifically focused on help the programming part of the data scientist. [\[1\]](#ludwig-a-code-free-deep-learning-toolbox) [\[4\]](#fklearn-a-functional-library-for-machine-learning)
* Technical issues in specific models were issued mainly in two talks. 
	* Multitask can be used to solve several problems at the same time helping the model to make quick classification since it shares the convolution layers for different tasks therefore indicating that the convolution really generalized the data. [\[5\]](#multitask-convolutional-neural-networks-saving-gpu-time)
	* Attention models were pointed as a solution to 'embedded' dynamically relational data values into a dense vector to help classifications tasks. [\[9\]](#attention-based-neural-networks-for-relational-data)
* Model interpretability was discussed much more as a reminder that the final user might not fully understand that a model is making decisions and classifications based on its input. The talks mostly pointed that is important to let the final user know which data is being used and how the model ended up getting to that value. [\[6\]](#ai-informs-humans-choose----or-do-they)
* Model validation was treated again in this second day. The validation is first presented as it is treated in academia and taught in the books and then the real world problems are brought upon. It's clear that are many things that must be adapted as no real world set-up can handle AB testing, for example. [\[7\]](#validating-models-in-the-real-world)

## My Watched Talks Index
<!-- MarkdownTOC autolink="true" -->

- [Ludwig, a Code-Free Deep Learning Toolbox](#ludwig-a-code-free-deep-learning-toolbox)
- [DataOps architecture for Machine Learning](#dataops-architecture-for-machine-learning)
- [AI culture at Dafiti and semi-autonomous review approval](#ai-culture-at-dafiti-and-semi-autonomous-review-approval)
- [FKLearn: A functional library for machine learning](#fklearn-a-functional-library-for-machine-learning)
- [Multitask convolutional neural networks: saving GPU time](#multitask-convolutional-neural-networks-saving-gpu-time)
- [AI informs, humans choose -- or do they?](#ai-informs-humans-choose----or-do-they)
- [Validating models in the real world](#validating-models-in-the-real-world)
	- [Supervised Learning in ML101](#supervised-learning-in-ml101)
	- [Supervised Learning in Real World](#supervised-learning-in-real-world)
	- [Model degradation](#model-degradation)
	- [Old Policies and bias:](#old-policies-and-bias)
	- [Engineering](#engineering)
	- [Business](#business)
- [Trading strategies using deep reinforcement learning](#trading-strategies-using-deep-reinforcement-learning)
- [Attention Based Neural Networks for Relational Data](#attention-based-neural-networks-for-relational-data)
- [Grupo ZAP](#grupo-zap)
- [Machine Learning for Natural Resources](#machine-learning-for-natural-resources)

<!-- /MarkdownTOC -->



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
**Carlos Porto Filho, Gustavo Castilhos** - *Data Scientist, Everis* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/6e/everis_DataOps_Noronha_PAPIs_v1.pptx)
* When a ML project is done? When it reaches 100% acc? When the deadline has passed?
* Why is it so hard to answer that? Business explain the requirements for the DS, the model is developed, but when it is deployed many integrations and iterations are really due to errors


----


## AI culture at Dafiti and semi-autonomous review approval
**Ricardo Savil** - *Data Scientist, Dafiti Group* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/f3/Dafiti%20%40%20papis.io_%20AI%20%26%20case.pdf)

* Ideation -> Detailing (Business Understanding) -> Prioritizing (Score projects and focus on a few) -> PoC (map and experiment)-> Implement (take the experimentation to the main teams) -> Finalization (approval with the business team)


----


## FKLearn: A functional library for machine learning
**Henrique Lopes** - *Machine Learning Engineer, Nubank*

Tutorial on the FKLearn developed by Nubank. Mostly tutorial/quick hands-on. The library has mostly been built on top of other known libraries but focusing on the versatility to call functions and ease the pipeline construction.


----


## Multitask convolutional neural networks: saving GPU time
**Paulo Eduardo Sampaio** - *Data science specialist, McKinsey & Company* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/86/multitask_papis.pdf)
* Single Task Classifier vs Multi Task Classifier
* Single > Input > Conv > Output
* Multi > Input > Conv > [Out1, Out2, Out3, ...]
* Iterator easier than hardcoded becaus it can handle settings like random seed, batch sizes, etc
* The losses can be different so the main loss of the model is the sum of them
* Using the CNN output as embedding and use a single multi-classify output


----


## AI informs, humans choose -- or do they?
**Bianca Ximenes** - *Independent consultant / Doctoral Student, Tecnora / UFPE* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/af/AI%20informs%2C%20humans%20choose.pdf)
* How Google makes trustable models
* <https://pair.withgoogle.com/>
* What is a mental model? 
* The product must ensure that the expectations of the user are aligned with the output of the model
* What is an AI? Is it going to improve? Is the product learning from my feedback?
* Is the user aware of what he can and cannot do with your model? Is it clear in the output?
* Explainability: Why did you output this prediction to this user?


----


## Validating models in the real world
**Luis Moneda** - *Data Scientist, Nubank* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/67/Papis%20-%20Validating%20models%20in%20the%20real%20world.pdf)
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
How often can I update my model? Is there any time constraint? This influences your timed train-test-validation set split in [Supervised Learning in Real World](#supervised-learning-in-real-world)

### Business
Lots of things can change in the X distribution. You can't do but you can monitor the changes to act with policies depending on the impact

<http://lgmoneda.github.io>


-----


## Trading strategies using deep reinforcement learning
**Suraj Shinde, Cristyan Ruffino Gil Morales** - *Director - AI Digital Lab, EVERIS MEXICO S DE RL DE CV, AI Research Lab Leader, everis*

Mainly based on internet tutorials like <https://www.youtube.com/watch?v=05NqKJ0v7EE>. 

|Market Data -> 			|\|Neural Model | -> Output (Buy, Sell, Hold)
|News Data -> Embedding ->	|\|			  |



----



## Attention Based Neural Networks for Relational Data
**Scott Brownlie** - *Senior Data Scientist, TOTVS Labs* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/1a/Attention-Based%20Neural%20Networks%20for%20Relational%20Data.pptx)
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