---
layout: post
title:  "Coursera NLP Module 2 Week 1 Notes"
ref: coursera-nlp-2-1
lang: en
categories: en
tags: deep-learning lecture-notes coursera nlp
datePublished: 2020-09-06T12:51:00-03:00
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

## Overview
* What is autocorrect?
* Building the model
* Minimum Edit Distance
* Minimun Edit Distance Algorithm

## Autocorrect

Application that changes mispelled words to the correct ones.

1. Indentify a misspelled word
2. Find strings n edit distance away
3. Filter candidates
4. Calculate word probabilities

## Building the model

1. You know misspelled words by looking into a dictionary. 
2. Edit Distance takes into consideration 3 operations:
   * Insert (add a letter)
   * Delete (remove a letter)
   * Switch (swap two neighbor letter)
   * Replace (replacing a letter)
3. Filter candidates looking into the dictionary

## Building the model II
4. Calculate the word probabilities

$$P(w) = \frac{C(w)}{V} $$

## Minimum edit distance

The lowest number to transform one string to another

## Minimum edit distance algorithm

$$    

D[i,j] = \left\{
   \begin{array}{lc}
     D[i-1, j] + del\_cost \\
     D[i, j-1] + ins\_cost \\
     D[i-1, j-1] + \left\{
      \begin{array}{rr}
      rep\_cost; if scr[i] \neq tar[j] \\
      0; if scr[i] = tar[j]
      \end{array}
      \right .
   \end{array}
   \right .
$$

## Ungraded Lab: Building the vocabulary

[Notebook](/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W1_lecture_nb_01.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W1_lecture_nb_01.ipynb)

## Ungraded Lab: Candidates from edits

[Notebook](/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W1_lecture_nb_02.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Ungraded%20Labs/NLP_C2_W1_lecture_nb_02.ipynb)

## Programming Assignment: Autocorrect

[Notebook](/assets/notebooks/NLP_specialization/Solved/C2_W1_Assignment.ipynb) / [HTML](https://github.com/marcossilva/marcossilva.github.io/blob/master/assets/notebooks/NLP_specialization/Solved/C2_W1_Assignment.ipynb)