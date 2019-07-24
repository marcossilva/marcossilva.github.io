---
layout: post
title:  "Coursera Deep Learning Module 2 Week 2 Notes"
ref: coursera-deep-learning-2-2
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-07-17T02:25:00-03:00
dateModified: 2019-07-17T02:25:00-03:00
description: Notes of the second Coursera module, week 2 in the deeplearning.ai specialization
image: /assets/Course2.png
---

{% include figure.html filename="Course2" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Improving Deep Neural Networks" width="50%" %}

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

## Mini-batch gradient descent

* Vectorization allows you to efficiently compute on m examples. But m if is really large that can still be slow. A solution to this is only ingest a small fixed amount of examples (1000, for example) and use each one to iteratively compute the errors.
* Notation: 
	- $x^{(i)}$ ith example in the test set
	- $Z^{[l]}$ lth layer in the neural network
	- $X^{\{i\}}$ ith batch in the mini-batch test set. $X^{\{i\}}.shape = (n_{x}, m)$