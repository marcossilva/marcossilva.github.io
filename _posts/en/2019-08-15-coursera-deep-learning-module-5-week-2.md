---
layout: post
title:  "Coursera Deep Learning Module 5 Week 2 Notes"
ref: coursera-deep-learning-5-2
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-08-16T01:54:00-03:00
dateModified: 2019-08-16T01:54:00-03:00
description: Notes of the fifth Coursera module, week 1 in the deeplearning.ai specialization
image: /assets/course5.jpeg
---

{% include figure.html filename="course5" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Recurrent Neural Network" width="50%" %}

<style type="text/css">
	div.code-highlited-mod{font-family:monospace;font-size: 15px;border: 1px solid #e8e8e8;border-radius: 3px;background-color: #eef;padding: 8px 12px;overflow-x: auto;}
</style>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

{% include prevnext.html prev="/en/2019/08/12/coursera-deep-learning-module-5-week-1.html" 
next="/en/2019/08/17/coursera-deep-learning-module-5-week-3.html" %}
## Word Representation

One hot vectors works well for small vocabularies and with words that have no strong correlation with any other. Word embeddings allows the dimensions of the representations used in the words to be much denser and to represent these relations better.

## Using word embeddings

Word embeddings can be used with transfer learning easily using the following steps:

1. Learn embeddings from a large text corpus (1-100B words) (or download pre-trained embedding online)

2. Transfer embedding to new task with smaller training set (say 100k words)

3. Optional: Continue to finetune the word embeddings with new data

Transfer learning has been used widely with Named Entity Recognition (NER), text summarization, Co-Reference Resolution, Parsing but not among machine translation or language modeling because of the difference in data volume.

## Properties of word embeddings
Although we can verify the parallelogram correlation (man is to female as king is to queen) in the original embedding space it's usually hard for us to visualize that. Using t-SNE technique is a solution but with it the parallelogram correlation doesn't work visually anymore.

Cosine Similarity:

$ sim(u, v) = \frac{u^Tv}{\lvert \lvert u \rvert \rvert_2 \lvert \lvert v \rvert \rvert_2}$


Reference: {% include link.html href="https://www.aclweb.org/anthology/N13-1090" title="Linguistic Regularities in Continuous Space Word Representations by Tomas Mikolov, Wen-tau Yih, Geoffrey Zweig"%}

## Embedding matrix
Given a matrix $E \in \mathbb{R}^{(n_{dimensions}, n_{words})}$ and a one-hot vector $o_j \in \mathbb{R}^{(n_{words}, 1)}$ we can obtain $E * o_j = e_j \in \mathbb{R}^{(n_{dimensions}, 1)}$

## Learning word embeddings

In the process of learning embeddings we pick a given word and try to predict its surrounds words (or vice versa). Although some neighbors context are the most commonly used we can also extract knowledge using variations like only using the last word.

## Word2Vec
Given a skip-gram you have a context word and is trying to predict the words around it (target) in a given range (+- 10 words, for example). Suppose you have 10k words in your vocabulary than the output function is expressed as:

$ p(t \| c) = \frac{e^{\theta_{t}^{T} e_c}}{\sum_{j=1}^{10k} e^{\theta_{j}^{T} e_c}}$

As this can be quite expensive since the number of classes is proportional to the number of words it can take a very long time to converge. To help with that an hierarchical softmax can be implemented where it predicts weather the output is in the first or second half of the words, for example. With a balanced binary tree there's a complexity os logn instead of n in the classifier.

Paper: {% include link.html href="https://arxiv.org/pdf/1301.3781" title="Efficient Estimation of Word Representations in Vector Space 2013 by Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean"%}

## Negative Sampling
Pick a context word and a desired target word as 1st example. Then take randomly other k words which are not the target and use them as negative samples. The guideline for k varies with the dataset size. Big datasets requires smaller ks (2-5) and small datasets requires big ks (5-20)

$P(y = 1 \| c, t) = \sigma(e^{\theta_{t}^{T} e_c})$ where $\theta_{t}$ represents each possible target word and $e_c$ for each possible context word. With this scenario you move from classifying 10k outputs in the softmax layer to 10k binary classification problems which are much easier to train. As guideline for the probability of sampling the words the authors proposed the following equation:

$P(w_i) = \frac{f(w_i)^{3/4}}{\sum_{j=1}^{10k} f(w_j)^{3/4}}$


Paper: {% include link.html href="https://arxiv.org/pdf/1310.4546" title="Distributed Representations of Words and Phrases and their Compositionality 2013 by Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean"%}

## GloVe word vectors

Constructing the matrix where $X_{ij}$ is given by the # of times i appears in context of j. Naturally $X_{ij} = X_{ji}$ Given this matrix we want to minimize the following sum:

$\sum_{i=1}^{10k} \sum_{j=1}^{10k} f(X_{ij}) (\theta_{i}^{T} e_j + b_i - b_j^{\'} - log X_{ij})^2$

Because $\theta_{i}^{T} e_j$ can be seen as any combination of orthogonal axis in the given dimension we cannot guarantee that the axis learned are interpretable. But it can be guaranteed that they might exist and that the parallelogram map still works.

Paper: {% include link.html href="https://www.aclweb.org/anthology/D14-1162" title="GloVe: Global Vectors for Word Representation 2013 by Jeffrey Pennington, Richard Socher, Christopher D. Manning"%}

## Sentiment Classification

Sentiment classification is the task of looking at a piece of text and telling if someone likes or dislikes the thing they're talking about.

A simple model would be:
1. Take the words of the review and get the embeddings
2. Average all the embeddings
3. Feed this averaged vector to a softmax that outputs the number of stars left by the client

The problem with this simple model is that it doesn't take in consideration the order of words, therefore will give some incorrect predictions if the review is composed mostly of "good" words but have a word which negate all the good to bad.

To overcome that an RNN can be used since it takes in consideration the past as seen previously. This architecture can be a many-to-one as we only want to predict the stars.

## Debiasing word embeddings

{% include figure.html filename="bias" extension="png" %}


Paper: {% include link.html href="https://arxiv.org/pdf/1607.06520" title="Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings 2016 by Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, Adam Kalai"%}

## Quiz

1.Suppose you learn a word embedding for a vocabulary of 10000 words. Then the embedding vectors should be 10000 dimensional, so as to capture the full range of variation and meaning in those words.
* [ ] True
* [X] False

2.What is t-SNE?
* [ ] A linear transformation that allows us to solve analogies on word vectors
* [X] A non-linear dimensionality reduction technique
* [ ] A supervised learning algorithm for learning word embeddings
* [ ] An open-source sequence modeling library

3.Suppose you download a pre-trained word embedding which has been trained on a huge corpus of text. You then use this word embedding to train an RNN for a language task of recognizing if someone is happy from a short snippet of text, using a small training set.

x (input text)	y (happy?)
I'm feeling wonderful today!	1
I'm bummed my cat is ill.	0
Really enjoying this!	1
Then even if the word “ecstatic” does not appear in your small training set, your RNN might reasonably be expected to recognize “I’m ecstatic” as deserving a label y = 1.
* [X] True
* [ ] False

4.Which of these equations do you think should hold for a good word embedding? (Check all that apply)


* [X] $e_{boy} - e_{girl} \approx e_{brother} - e_{sister}$
* [ ] $e_{boy} - e_{girl} \approx e_{sister} - e_{brother}$
* [X] $e_{boy} - e_{brother} \approx e_{girl} - e_{sister}$
* [ ] $e_{boy} - e_{brother} \approx e_{sister} - e_{girl}$


5.Let EE be an embedding matrix, and let $o_{1234}$ be a one-hot vector corresponding to word 1234. Then to get the embedding of word 1234, why don’t we call E * $o_{1234}$ in Python?
* [ ] It is computationally wasteful.
* [X] The correct formula is $E^T* o_{1234}$
* [ ] This doesn’t handle unknown words (<UNK>).
* [ ] None of the above: calling the Python snippet as described above is fine.

6.When learning word embeddings, we create an artificial task of estimating P(target∣context). It is okay if we do poorly on this artificial prediction task; the more important by-product of this task is that we learn a useful set of word embeddings.
* [X] True
* [ ] False

7.In the word2vec algorithm, you estimate P(t∣c), where t is the target word and c is a context word. How are t and c chosen from the training set? Pick the best answer.
* [ ] c is the sequence of all the words in the sentence before t.
* [X] c and t are chosen to be nearby words.
* [ ] c is a sequence of several words immediately before t.
* [ ] c is the one word that comes immediately before t.

8.Suppose you have a 10000 word vocabulary, and are learning 500-dimensional word embeddings. The word2vec model uses the following softmax function:

$ p(t \| c) = \frac{e^{\theta_{t}^{T} e_c}}{\sum_{j=1}^{10k} e^{\theta_{j}^{T} e_c}}$
Which of these statements are correct? Check all that apply.
* [X] $\theta_t$ and $e_c$ are both 500 dimensional vectors.
* [ ] $\theta_t$ and $e_c$ are both 10000 dimensional vectors.
* [X] $\theta_t$ and $e_c$ are both trained with an optimization algorithm such as Adam or gradient descent.
* [ ] After training, we should expect $\theta_t$ to be very close to $e_c$ when t and c are the same word.

9.Suppose you have a 10000 word vocabulary, and are learning 500-dimensional word embeddings.The GloVe model minimizes this objective:

$min \sum_{i=1}^{10k} \sum_{j=1}^{10k} f(X_{ij}) (\theta_{i}^{T} e_j + b_i - b_j^{\'} - log X_{ij})^2$
Which of these statements are correct? Check all that apply.
* [X] $\theta_i$ and $e_j$ should be initialized to 0 at the beginning of training.
* [ ] $\theta_i$ and $e_j$ should be initialized randomly at the beginning of training.
* [X] $X_{ij}$ is the number of times word i appears in the context of word j.
* [X] The weighting function $f(.)$ must satisfy $f(0) = 0$

10.You have trained word embeddings using a text dataset of $m_1$ words. You are considering using these word embeddings for a language task, for which you have a separate labeled dataset of $m_2$ words. Keeping in mind that using word embeddings is a form of transfer learning, under which of these circumstance would you expect the word embeddings to be helpful?
* [X] $m_1$ >> $m_2$
* [ ] $m_1$ << $m_2$


{% include prevnext.html prev="/en/2019/08/12/coursera-deep-learning-module-5-week-1.html" 
next="/en/2019/08/17/coursera-deep-learning-module-5-week-3.html" %}