---
layout: post
title:  "Coursera Deep Learning Module 5 Week 1 Notes"
ref: coursera-deep-learning-5-1
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-08-12T02:08:00-03:00
dateModified: 2019-08-12T02:08:00-03:00
description: Notes of the fifth Coursera module, week 1 in the deeplearning.ai specialization
image: /assets/course4.jpeg
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

## Why sequential models

Work best with sequential data as:
* Speech Recognition
* Music Generation
* Sentiment Classification
* DNA Sequence Analysis
* Machine Translation
* Video Activity Recognition
* Name Entity Recognition

The given inputs may or may not be of the same kind or even have the same length.

## Notation

Given an input x we would have $x^{\<i\>}$ as the ith word in the sentence, for example. $T_x$ denote how long the sequence is. In named entity recognition we could have the same length in the output denoted by $T_y$ where each $y^{\<i\>}$ denotes a given output.

A common way to vectorize the given input $x^{\<i\>}$ is using one hot encoded vectors. In this encoding each position of the vector represent a word. 

## Recurrent Neural Network Model

{% include figure.html filename="unrolled_rolled" extension="png" alt="Unrolled and Rolled diagram of an RNN" title="Unrolled and Rolled diagram of an RNN" caption="Unrolled and Rolled diagram of an RNN" %}

A limitation of this type of network is that only uses information from the past of the sequences.

* $a^{\<0\>} = \overrightarrow{0}$
* $a^{\<t\>} = g_1(W_{aa} a^{\<t-1\>} + W_{ax} x^{\<t\>} + b_a)$
* $\hat{y}^{\<t\>} = g_2(W_{ya} a^{\<t\>} + b_y)$

* $a^{\<t\>} = g_1(W_{a} [a^{\<t-1\>} ,x^{\<t\>}] + b_a)$
* $[W_{aa} W_{ax}] = W_a$

## Backpropagation through time
The loss for each time step prediction can be given as $\mathcal{L}(\hat{y}^{\<t\>}, y^{\<t\>}) = - y^{\<t\>}\log\hat{y}^{\<t\>} - (1-y^{\<t\>})\log(1-\hat{y}^{\<t\>})$ and the overall loss is simply the sum of each time step as $\mathcal{L}(\hat{y}, y) = \sum_{t=1}^{T_y} \mathcal{L}(\hat{y}^{\<t\>}, y^{\<t\>})$.

## Different types of RNNs

$T_x$ and $T_y$ might not always be the same.

{% include figure.html filename="diags" extension="jpg" alt="Different types os architecture organization in seq2se1 models" title="Different types os architecture organization in seq2se1 models" caption="Each rectangle is a vector and arrows represent functions (e.g. matrix multiply). Input vectors are in red, output vectors are in blue and green vectors hold the RNN's state (more on this soon). From left to right: (1) Vanilla mode of processing without RNN, from fixed-sized input to fixed-sized output (e.g. image classification). (2) Sequence output (e.g. image captioning takes an image and outputs a sentence of words). (3) Sequence input (e.g. sentiment analysis where a given sentence is classified as expressing positive or negative sentiment). (4) Sequence input and sequence output (e.g. Machine Translation: an RNN reads a sentence in English and then outputs a sentence in French). (5) Synced sequence input and output (e.g. video classification where we wish to label each frame of the video). Notice that in every case are no pre-specified constraints on the lengths sequences because the recurrent transformation (green) is fixed and can be applied as many times as we like." %}

Reference: {% include link.html href="http://karpathy.github.io/2015/05/21/rnn-effectiveness/" title="The Unreasonable Effectiveness of Recurrent Neural Networks 2015 blog post by Andrej Karpathy"%}