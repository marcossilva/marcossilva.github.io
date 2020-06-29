---
layout: post
title:  "Coursera NLP Module 1 Week 1 Notes"
ref: coursera-deep-learning-1-1
lang: en
categories: en
tags: deep-learning lecture-notes coursera nlp
datePublished: 2020-06-28T01:54:00-03:00
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

## Supervised ML & Sentiment Analysis

![](/assets/2020-06-28-15-20-37.png)

## Vocabulary & Feature Extraction

* **Vocabulary** : All the unique words on your corpus
* **One-hot encoding**: Taking a given input text and a given know vocabulary and marking with 1 where the words on your input text show up on a given position in your vocabulary. The output has dimension $\|V\|$ given by the size of the vocabulary. Usually the output is sparse as the vocabulary is usually large. This technique also don't address the order os the words.

## Negative and Positive Frequencies

Given a set of inputs/tweets classified as positive or negative we can count the words in a given tweet as their frequency in the known classes.

![](/assets/2020-06-28-15-29-01.png)

## Feature Extraction with Frequencies

Now, given that the only classes are positive and negative it's possible to output a given vector with the frequency of the classes. The words should only be accounted once even if they repeat.

![](/assets/2020-06-28-15-31-25.png)

## Preprocessing

* **Stop Words**: words that do not aggregate meaning to the given sentence. Usually connectives and prepositions.
* **Puntuaction**: symbols that do not aggregate meaning to the given sentence. Usually are part of URLs or other forms of expression that not words (emphasis, emojis)
* **Stemming**: Leaving only the radical of the word in the output. Multiple conjugations and people flexions have the same radical therefore easening the learning.
* **Lowercasing**: Normalization of the given input to a single type of character.

![](/assets/2020-06-28-15-32-54.png)
![](/assets/2020-06-28-15-35-21.png)

## Natural Language preprocessing

[Ungraded Lab 1](/assets/notebooks/NLP_specialization/Ungraded Labs/NLP_C1_W1_01_Preprocessing.ipynb) [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded Labs/NLP_C1_W1_01_Preprocessing.ipynb)

## Putting it All Together
Pipeline to extract the features for a set of tweets.

![](/assets/2020-06-28-15-38-13.png)

## Visualizing word frequencies

[Ungraded Lab 2](/assets/notebooks/NLP_specialization/Ungraded Labs/NLP_C1_W1_02_WordFreqs.ipynb) [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded Labs/NLP_C1_W1_02_WordFreqs.ipynb)

## Logistic Regression: Testing

Given a trained 

![](/assets/2020-06-28-15-40-33.png)

![](/assets/2020-06-28-15-40-47.png)

![](/assets/2020-06-28-15-41-04.png)

## Logistic Regression: Cost Function

The first term focus on how much it agrees with the positive data classification. The second term balance with the negative data classification. Here they have the same relationship but given a different penalty one could be maximized better than the other if desired.

![](/assets/2020-06-28-16-05-24.png)

## Assignment: Logistic Regression

[Graded Lab](/assets/notebooks/NLP_specialization/Solved/C1_W1_SentimentAnalysis_logregression.ipynb) [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Solved/C1_W1_SentimentAnalysis_logregression.ipynb)