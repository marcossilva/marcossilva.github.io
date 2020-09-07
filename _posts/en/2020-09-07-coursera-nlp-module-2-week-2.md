---
layout: post
title:  "Coursera NLP Module 2 Week 2 Notes"
ref: coursera-nlp-2-2
lang: en
categories: en
tags: deep-learning lecture-notes coursera nlp
datePublished: 2020-09-07T12:39:00-03:00
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

## Part of Speech Tagging

* What is part of speech tagging
* Markov chains
* Hidden Markov models
* Viterbi models

Part-of-speech refers to the category of words or the lexical terms in the language. Examples of these lexical terms in the English language would be noun, verb, adjective, adverb, pronoun, preposition, although there are many others.

## Markov Chains

**Markov property**: the probability of the next event only depends on the current events.

![](/assets/2020-09-06-17-18-33.png)
![](/assets/2020-09-06-17-18-45.png)

Emission probabilities are the probabilities to the observables, the words in the input. 

![](/assets/2020-09-06-17-22-56.png)
![](/assets/2020-09-06-17-26-20.png)

### Populating the Transition Matrix
Smoothing can be added to avoid zero division and help generalization. Smoothing can't be done with the first row $ \pi $, tough, as it could allow the sentence to start with punctiation, for example.
![](/assets/2020-09-06-17-32-05.png)

### Populating the Emission Matrix
![](/assets/2020-09-06-17-37-03.png)

## The Viterbi Algorithm

It's a graph algorithm.

### Initialization step
   
![](/assets/2020-09-06-17-59-20.png)
![](/assets/2020-09-06-17-59-33.png)

### Forward pass


![](/assets/2020-09-06-17-58-59.png)

### Backward pass
Calculate the index of the biggest probability in the last step and backward get the steps accordingly in the D matrix.

![](/assets/2020-09-06-18-02-21.png)

![](/assets/2020-09-06-18-05-25.png)


Log probabilities help the problem of consecutive multiplication of small numbers.

![](/assets/2020-09-07-00-38-36.png)


## Ungraded Lab: Working with text data

[Notebook](/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W2_lecture_notebook_numpy.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W2_lecture_notebook_numpy.ipynb)

## Ungraded Lab: Working with text data

[Notebook](/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W2_lecture_notebook_strings_tags.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W2_lecture_notebook_strings_tags.ipynb)

## Programming Assignment: Autocorrect

[Notebook](/assets/notebooks/NLP_specialization/Solved/C2_W2_Assignment.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Solved/C2_W2_Assignment.ipynb)