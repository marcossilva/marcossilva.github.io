---
layout: post
title:  "Notes on PAPIs.io (Day 1)"
ref: papis-1
lang: en
categories: en
tags: 
datePublished: 2019-06-25T18:00:00-03:00
dateModified: 2019-06-25T18:00:00-03:00
description: Main topics summary of the watched talks in the first day on presentations in PAPIs.io
image: /assets/papis.png
---
<div style="background-color: black;">
<a href='https://papis.io'>
{% include figure.html filename="papis" extension="png" alt="logo of the papis conference" title="PAPIs.io Conference" caption="PAPIs.io"%}</a></div>

PAPIS.io is the main conference on Machine Learning applied to the market in the Latim America. It took place in São Paulo 25 and 26th June at the Cinemark Eldorado. This year I had the amazing oportunity to participate through B2W sponsorship. The conference takes place mainly to allow the data science related public to share results and opinions and also to increase the networking between the professionals of the area. The attending public varies wildly between:
* Engineers
* Scientists
* Managers
* Hackers
* Researchers

The chairs pointed out an increase in the knowledge level of participants since last year from intermediate to advanced.
Diversity at PAPIs: 55 tickets to diversity applicants and 24% of speakers are women.

The first day of PAPIs.io was full of amazing presentations. Among the top knowledges I've gathered from all these talks I can pinpoint:

* Incremental knowledge is a common thing in data science. Either to develop your model or your comprehension of the data and your final client. {% include link.html text='2' href='#lessons-learned-from-building-a-credit-card-fraud-model) {% include link.html text='3' href='#bias-and-bugs-implementing-recommendations' target='_self' %}
* There are problems with the classic AB testing proposed in academia applied to the market. AB testing is mainly designed to test visual features but when used in the real world with changes all the time it can be pretty tricky. AB testing also shouldn't be used to predict the behavior of any given KPI as it is not the main intended reason behind it. {% include link.html text='3' href='#bias-and-bugs-implementing-recommendations) {% include link.html text='4' href='#where-are-the-gains-should-i-use-ab-tests-for-forecasting' target='_self' %}
* The right solutions should be used in the right applications. Many developers or scientists end up trying to build a perfect system and fail or loose too much time on it. There's a correct use for each available tool and a correct application can be found given the correct restrictions. {% include link.html text='5' href='#tensorflow-image-inferencing-an-adventure-in-python-and-go) {% include link.html text='6' href='#deploy-your-deep-learning-models-in-serverless-architectures' target='_self' %}
* Prediction systems have a wide possibility of usage and can be deployed as complex as the system requires. {% include link.html text='9' href='#time-series-forecasting-for-cloud-resources-provisioning' target='_self' %}

## My Watched Talks Index
- {% include link.html href='#real-life-reinforcement-learning' text='Real life Reinforcement Learning' %}
	- {% include link.html href='#applications' text='Applications' %}
	- {% include link.html href='#references' text='References' %}
- {% include link.html href='#lessons-learned-from-building-a-credit-card-fraud-model' text='Lessons Learned from Building a Credit Card Fraud Model' %}
	- {% include link.html href='#impact-of-fraud-on-merchants' text='Impact of fraud on merchants' %}
	- {% include link.html href='#machine-learning-to-rescue' text='Machine Learning to Rescue' %}
	- {% include link.html href='#importance-of-unbiased-data' text='Importance of unbiased data' %}
	- {% include link.html href='#initial-attempt' text='Initial attempt' %}
	- {% include link.html href='#final-thoughts' text='Final Thoughts' %}
- {% include link.html href='#bias-and-bugs-implementing-recommendations' text='Bias and Bugs: implementing recommendations' %}
- {% include link.html href='#where-are-the-gains-should-i-use-ab-tests-for-forecasting' text='Where are the gains: Should I use A/B tests for Forecasting?' %}
	- {% include link.html href='#predictive-model' text='Predictive Model' %}
	- {% include link.html href='#when-should-the-forecasting-be-done' text='When should the forecasting be done?' %}
	- {% include link.html href='#final-thoughts-1' text='Final Thoughts' %}
- {% include link.html href='#tensorflow-image-inferencing-an-adventure-in-python-and-go' text='TensorFlow image inferencing: an adventure in Python and Go' %}
	- {% include link.html href='#final-thoughts-2' text='Final Thoughts' %}
- {% include link.html href='#deploy-your-deep-learning-models-in-serverless-architectures' text='Deploy your Deep Learning models in serverless architectures' %}
	- {% include link.html href='#available-solutions' text='Available Solutions' %}
	- {% include link.html href='#what-is-serverless' text='What is serverless?' %}
	- {% include link.html href='#how-do-i-do-a-serverless-ml-application' text='How do I do a serverless ML application?' %}
	- {% include link.html href='#price-comparison' text='Price comparison' %}
- {% include link.html href='#using-machine-learning-to-recommend-jobs-in-user-cold-start' text='Using Machine Learning to recommend jobs in User Cold Start' %}
- {% include link.html href='#a-clinical-application-of-deep-learning-for-nlp-with-word-embeddings' text='A Clinical Application of Deep Learning for NLP with Word-Embeddings' %}
	- {% include link.html href='#references-1' text='References' %}
- {% include link.html href='#time-series-forecasting-for-cloud-resources-provisioning' text='Time Series Forecasting for Cloud Resources Provisioning' %}
- {% include link.html href='#how-big-data-powers-ambev-sales-machine---sponsored-by-big-data' text='How Big Data Powers Ambev Sales Machine - sponsored by Big Data' %}
- {% include link.html href='#how-ai-is-transforming-ifood-logistics---estimated-time-of-arrival-case' text='How AI is transforming iFood logistics - Estimated Time of Arrival Case' %}



## Real life Reinforcement Learning
**Julien Simon** - *Technical Evangelist*

With either supervised or unsupervised learning you need a dataset. But building a dataset isn't always an optimal. There are many large, complex problems; uncertain, chaotic environments. Learning without data is a natural task to us humans like walking or riding a bike. 

In basic reinforcement learning there's an agent that exists, observes and interact in an environment. Those interactions generate positive and negative rewards that, in a loop, give them the ability to learn.

Initially the agent takes random actions and gathering its rewards. As we build episodes we build data. 

### Applications

Stock Market Prediction
Neural Network Compression (Layer Removal without accuracy loss)
Delivery Planning Optimization
Autonomous Car Simulation

### References:
{% include link.html href='https://aws.amazon.com/machine-learning/' %}


----


## Lessons Learned from Building a Credit Card Fraud Model
**Leela Senthil Nathan** - *Software Engineer, Stripe* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/b2/PAPIs%20Credit%20Card%20Fraud%20Detection.key' text='PDF Presentation' %}
### Impact of fraud on merchants
* Fraudsters uses stolen card to buy item online
* Customer contacts bank to dispute transaction
* Bank confirm fraudulent transaction
* Merchant is left with prejudice

### Machine Learning to Rescue
* Easy to build model in isolation
* Major real-problems:
	1. Data imbalance. Most of the transactions recorded are correct transactions. 
		* TP = Fraud correctly identified and blocked. 
		* FP = Fraud incorrectly identified and correct transaction
		* TN = Fraud correctly not identified and not blocked
		* FN = Fraud incorrectly not identified and not blocked
	* Model outputs score
	* Binary Classifier
	* Sensitive to FPR but sensitive to Recall as possible
	* FPR = FP/(FP+TN)
	* **Solution**: Downsample the negative class (non-fraudulent transaction)
	2. Merchants aren't experts at evaluating model
		* Conterfactual evaluation: What would have happened if we just had left the transaction happen?

### Importance of unbiased data
* We can only train on unblocked transactions
* As the model blocks the 'easy' frauds and you gather more data on the 'hard' frauds you end up with a model that 'forgets' how to block the easy ones and end up blocking just hard ones.

### Initial attempt
* P(allow) to let some of the fraudulent through with an inversely proportional probability curve
* The problem with this approach is that it supposes that the model is performing well.
* Supposing the score can be used as a threshold again as a binary problem classification it's much easier to have a binary step function with the x% allowance in the P(allow)

### Final Thoughts
* Experiment a lot. Imbalanced data doesn't help machine learning algorithms to learn anything at all

----

## Bias and Bugs: implementing recommendations
**Guilherme Silveira** - *Alura* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/f4/Bias%20and%20Bugs_%20implementing%20recommendations.pdf' text='PDF Presentation' %}
* Human Benchmark as Baseline
* Correlation != Causation
* Bayes-Based AB Test?
* Randomness on group selection

----

## Where are the gains: Should I use A/B tests for Forecasting?
**Eder Martins** - *Data scientist, SEEK*

* Good promises on the A/B test promises but as it gets into production the KPIs fall down and everyone gets stressed
* Promising solution -> Offline tests -> A/B tests -> Shipping to production
* A/B Test is a randomized experiment, relies on making one change and observing its influence
* The population should be statistically similar (size of population, demographic variables, etc)
* Even if the test gives us high p-values indicating growth (or decreases) there are many variables that affect the KPI externally
* Novelty Effect: The novelty effect, in the context of human performance, is the tendency for performance to initially improve when new technology is instituted, not because of any actual improvement in learning or achievement, but in response to increased interest in the new technology.
* A/B tests are great for comparing algorithms but it doesn't provide any insight in any KPI performance
* To predict how the KPI will perform it's better to use a prediction model

### Predictive Model

* Based on past data tries to predict future samples
* The prediction can also be in a given range
* Prophet, Hotwinters, ARIMA

### When should the forecasting be done?
* After the A/B test: Historical data -> A/B test (start) -> A/B test (end) -> Forecasting model
* During the A/B test: Historical data -> A/B test (start) -> Forecasting model (A and B separately)

### Final Thoughts
* Do not use A/B test to predict future
* Use forecasting models to predict KPI behavior in future


----


## TensorFlow image inferencing: an adventure in Python and Go
**Vitor De Mario** - *Tech Lead, NeuralMed* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/e8/vdemario_papis_tensorflow_inferencing_python_go.pdf' text='PDF Presentation' %}
### Final Thoughts
Use the right tool for the right job. It's undoubted that ML thrives in python but it's well known for many developers that other languages are better for some other ends. The best solution was not to use the newly created ported version of Tensorflow to Go, for example, but instead use the python one (which is much more well maintained) and plug the output in the Go existing structure.


----


## Deploy your Deep Learning models in serverless architectures
**Adriano Dennanni** - *Machine Learning Engineer, neuronio.ai* - [PDF Presentation](https://static.sched.com/hosted_files/papislatam2019/0f/Deploy%20your%20Deep%20Learning%20models%20in%20serverless%20architectures.pdf)

### Available Solutions
1. Virtual Machine: 
2. Virtual Machine (with GPU)
3. Container with Kubernetes
4. Services with Trained Models (Amazon Lex, Amazon Rekognition, GCP Speecht-to-Text)
5. Complex Solutions (FGPA, TPU, Vast.ai - GPU rental service)

### What is serverless?
* No server management
* Pay only what you consumes
* Flexible scalability
* High availability

### How do I do a serverless ML application?

* Cloud Functions (Lambda/Google Cloud Computing)
* Train the model
* Save the model on the storage
* Reload the model on the running service

### Price comparison
* CPU and GPU machines have different costs. Its much cheaper to have CPU-only machines to inferences but to training the GPU can easily overcome the performance by a far amount
* All the things are priced (accessing the storage, processing, saving, upscaling machines, deleting old ones, etc)
* Using Tensorflow Lite is lighter


----


## Using Machine Learning to recommend jobs in User Cold Start
**Andryw Marques** - *Data Scientist, SEEK* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/89/Papis%20-%20Andryw%20Marques%20-%20Cold%20Start.pdf' text='PDF Presentation' %}

* **Train data**: Applied position + randomly negativa non-applied position
* **Algorithm**: XGBoost (well known, used in Kaggle competitions with good results)
* **Evaluation**: Offline evaluation -> Visual evaluation -> 
	* Offline: Historical data, Precision and Coverage @ top 10 predictions
	* Online: A/A and A/B test


----


## A Clinical Application of Deep Learning for NLP with Word-Embeddings
**Arnon Santos** - *Data Scientist, Junto Seguros* - {% include link.html href='https://static.sched.com/hosted_files/papislatam2019/b8/ABVS_EMBEDDINGS_PAPIS.pdf' text='PDF Presentation' %}

What is clinical coding? Is the whole journey of a patient since it arrives in the hospital and leaves it. The clinical coding is the standardization of this whole process in a commons language to all the doctors. This is a super boring process that is currently done manually. 

The proposed approach is to use the word embeddings and convolve on them to classify all the documents and classify into one of the ICD-10 codes. This is a code to easily identify the disease.

Next steps: increase to the complete set of ICD codes.

### References:
Paper: Using Deep Convolutional Neural Networks with Self-Taught Word Embeddings


----


## Time Series Forecasting for Cloud Resources Provisioning
**Leonardo Neri** - *AI Manager, Accenture*

* **Available data**: 90 days of CPU and memory usage once per day
* **Augumented data**: Expansion of the data for 3 years based on the data distribution
* **Algorithm** Prophet: y(t) = g(t) + seasons(t) + holidays(t) -> Highly explainable

* Outputs:
	* Yearly seasonality: peaks on the holidays (Xmas, Mother's Day)
	* Week seasonality


----


## How Big Data Powers Ambev Sales Machine - sponsored by Big Data
**Gustavo Ioschpe** - *Founder & CEO, Big Data*

* Managers insist in using means when, most of the time, it doesn't adds real value or any guideline
* *Compra certa* helped to understand and cluster how each clients should buy beer given their clients location and consume habits
* Understand users
* Challenge the common sense
* Test, learn and improve
* Balance between Business and Algorithms / Empirical and Technical Skills


----


## How AI is transforming iFood logistics - Estimated Time of Arrival Case
**Arnaud Seydoux** - *Logistic IA manager, iFood*

* Evolving traditional static logistic to on demand
* New logistic: short time to deliver, cloud of drivers, unexpected events
* new solutions: stochastic dispatch, optimal driver repositioning (pricing), estimated time of arrival
* Delivery = max(assign + 1st mile, preparation time) + last mile

{% include figure.html filename="benchmark_evaluation" extension="jpg" alt="AB test showing that option A is better than B" title="AB test summary results" caption="AB test summary results"%}

{% include figure.html filename="monitoring" extension="jpg" alt="monitoring dashboard to keeo track of model performance in the deplyed application" title="Kibana boards with performance metrics" caption="Kibana boards with performance metrics"%}

{% include figure.html filename="model" extension="jpg" alt="neural network of the used model" title="Neural network of the used model" caption="Neural network of the used model"%}

{% include figure.html filename="prediction_architecture" extension="jpg" alt="Pipeline used to make prediction with the model. Graphite and Redis datasets are used to collect metrics which is then used in the prediction thread and published in the AWS cloud service." title="Pipeline used to make prediction with the model" caption="Prediction Pipeline"%}

* Saturation of Restaurant -> Time since last order, time since last order accepted, time since last order departed

| Results | Improvements|
| **Pickup ETA** | **Data is Key** |
| 1 minute saving on courier waiting time at restaurant: 250000 cost saving/month | more data at restaurant level |
| **Global ETA**  | **Operation** |
| 3% increase in SLA or 7 min decrease in promise customer satisfaction | couriers and restaurants behavior improvement |