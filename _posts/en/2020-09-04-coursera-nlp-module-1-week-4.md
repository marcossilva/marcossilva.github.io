---
layout: post
title:  "Coursera NLP Module 1 Week 4 Notes"
ref: coursera-nlp-1-4
lang: en
categories: en
tags: deep-learning lecture-notes coursera nlp
datePublished: 2020-09-04T12:51:00-03:00
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

## Machine Translation: An Overview

![](/assets/2020-09-04-00-58-30.png)

## Transforming word vector

Given a set of english words X, a transformation matrix R and a desired set of french word Y the transformation 
* $$ XR \approx Y $$
* We initialize the weights R randomly and in a loop execute the following steps
* $$ Loss = || XR - Y||_F $$
* $$ g = \frac{d}{dR} Loss $$
* $$ R = R - \alpha g $$

The Frobenius Norm takes all the squares of each elements of the matrix and sum them up. 

* $$ ||A||_F = \sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n} |a_{ij}|^2}$$

To simplify we can take the norm squared, thus:

* $$ ||A||^2_F = \sum_{i=1}^{m} \sum_{j=1}^{n} |a_{ij}|^2$$

Gradient:
* $$ g = \frac{d}{dR} Loss = \frac{2}{m} (X^T (XR-Y))$$

## Hash tables and hash functions
Hash might skip other proprieties of the itens being hashed.
![](/assets/2020-09-04-01-42-17.png)
To ensure that the itens are hashed accordingly we will use Locality sensitive hashing.
![](/assets/2020-09-04-01-41-53.png)

## Locality sensitive hashing
With multiple plans we can use a binary encoding to give the hash of the position given by the position.
![](/assets/2020-09-04-01-53-58.png)

## Ungraded Lab: Rotation Matrices in R2

[Notebook](/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C1_W4_01_VectorRotation.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C1_W4_01_VectorRotation.ipynb)

## Ungraded Lab: Hash Tables and Multiplanes

[Notebook](/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C1_W4_02_HashAndMultiplanes.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C1_W4_02_HashAndMultiplanes.ipynb)

## Programming Assignment: Word Translation

[Notebook](/assets/notebooks/NLP_specialization/Solved/C1_W4_Assignment.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Solved/C1_W4_Assignment.ipynb)