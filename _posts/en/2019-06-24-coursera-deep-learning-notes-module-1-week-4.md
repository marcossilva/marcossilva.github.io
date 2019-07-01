---
layout: post
title:  "Coursera Deep Learning Module 1 Week 4 Notes"
ref: coursera-deep-learning-1-4
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-06-24T02:25:00-03:00
dateModified: 2019-06-24T02:25:00-03:00
description: Notes of the first Coursera module, week 4 in the deeplearning.ai specialization
image: /assets/Course1-1.png
---

{% include figure.html filename="Course1-1" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Week 3 - Shallow Neural Networks" width="50%" %}

## Week 3 - Shallow Neural Network
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  displayAlign: "left"
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

### Deep L-Layer neural network

* $L = 4$ (# of layers)
* $n^{[l]} = $ #units in layers l
* $n^{[0]} = 3 \text{ (input layer) }, n^{[1]} = 5, n^{[2]} = 5, n^{[3]} = 3, n^{[4]} = 1 \text{ (output layer) }$
* $a^{[l]}$ (activation in layer l)
* $a^{[l]} = g^{[l]}(z^{[l]}), w^{[l]} = \text{ weights for } z^{[l]}, b^{[l]} = \text{ bias for } z^{[l]}$
* $a^{[4]} = \hat{y}$

### Forward Propagation in a Deep Neural Network

* $Z^{[l]} = W^{[l]}A^{[l-1]} + B^{[l]}$
* $A^{[l]} = g^{[l]}(A^{[l]})$

### Getting your matrix dimension right

* $Z^{[l]}.shape = (n^{[l]}, m)$
* $W^{[l]}.shape = (n^{[l]}, n^{[l-1]})$
* $A^{[l]}.shape = (n^{[l-1]}, m)$
* $dW^{[l]}.shape = (n^{[l]}, n^{[l-1]})$
* $db^{[l]}.shape = (n^{[l]}, m)$

### Why deep representations

* Compositional representation: Shallow networks are able to detect simple features, deep layers are able to detect complex functions and are able to model much more complex data from the simple features
* Circuit theory: There are functions you can compute with a "small" L-layer deep neural network that shallower networks require exponentially more hidden units to compute. e.g.: XOR detection: 2 layer 3-2-1 neurons vs 1 layer with $2^n$ neurons to map all the combinations of the inputs

