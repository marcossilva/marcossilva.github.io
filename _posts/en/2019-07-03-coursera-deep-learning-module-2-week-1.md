---
layout: post
title:  "Coursera Deep Learning Module 2 Week 1 Notes"
ref: coursera-deep-learning-2-1
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-07-03T02:25:00-03:00
dateModified: 2019-07-03T02:25:00-03:00
description: Notes of the second Coursera module, week 1 in the deeplearning.ai specialization
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

## Train/Dev/Test Sets

* Applied ML is a highly iterative process
* Start with an idea, implement it in a code and experiment
* Previous era: 70/30 or 60/20/20
* Modern big data era: 98/1/1 or 99.5/0.25/0.25
* The dev set is simply a way to compare the real performance across algorithms
* The test set is to guarantee the real generalization of the model
* Mismatched train/test distribution
	- Training set: Cat pictures from webpages
	- Dev/test set: Cat pictures from users using your app
	- Different resolutions, different image (data) quality
	- Make sure that dev and test set have the same distribution as your train set
* It might be okay not to have a test set but the evaluation must be made to a different data set which hasn't been seen by the model, like production

## Bias/Variance

* Underfitting x Overfitting
* Train set error: 1% x Dev set error: 11% -> High variance
* Train set error: 15% x Dev set error: 16%. Assuming that humans obtain error \~0% -> High Bias because the algorithm isn't even fitting the training set well
* Train set error: 15% x Dev set error: 30% -> High Bias and high variance
* Train set error: 0.5% x Dev set error: 1% -> Low bias and low variance
* All these assumptions are based on the assumption that the human error, or optimal base error is close to 0%

## Basic Recipe for Machine Learning

* High bias? (bad train data performance) -> Bigger Network, Train longer, NN Architecture Search
* High variance? (test set performance) -> More data, regularization, NN Architecture Search

## Regularization

* $minJ(w, b)$ where $J(w,b) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)})$
* $w \in \mathbb{R}^{n_x}, b \in \mathbb{R}$
* To add regularization to this function just add $\lambda$ like $ J(w,b) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}) + \frac{\lambda}{2m} \lvert w \rvert_{2}^{2} + \frac{\lambda}{2m} b^2 $
* $L_2$ regularization = $ \lvert \lvert w \rvert \rvert_{2}^{2} = \sum_{j=1}^{n_x} w_{j}^{2} = w^{T}w $
* $L_1$ regularization = $ \frac{\lambda}{m} \sum_{i=1}^{n_x} \lvert w \rvert = \frac{\lambda}{m} \lvert \lvert w \rvert \rvert_{1}$
* m or 2m in the denominator is just a scaling constant
* $\lambda$ is the regularization parameter and is another hyperparameter in the network
* $J(w^{[1]},b^{[1]}, ..., w^{[L]},b^{[L]}) = \frac{1}{m} \sum_{i=1}^{n} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}) + \frac{\lambda}{2m} \sum_{l=1}^{L} \lvert \lvert w^{[l]} \rvert \rvert_{F}^{2} $
* Frobenius Norm = $ \lvert \lvert w^{[l]} \rvert \rvert_{F}^{2} = \sum_{i=1}^{n^{[l-1]}} \sum_{j=1}^{n^{[l]}} (w_{ij}^{[l]})^{2}$
* $ w : (n^{[l]}n^{[l-1]})$
* $dW^{[l]}$ from backpropagation now becomes $dW^{[l]} + \frac{\lambda}{m}w^{[l]}$
* $L_2$ norm is also sometimes called weight decay
* The regularization multiplies the previous term for a number pretty close to 1, therefore only diminishing its impact

## Why regularization reduces overfitting?

* If $\lambda$ is really big the regularization is pushing the weights matrices really close to 0. If many of the weights are 0 is like the neurons are dead so it's pretty much like you have a much simpler network.
* Thinking with a $tanh$ activation function: if we only focus on variations really close to 0 the variation is roughly linear. If the activation is linear adding layers in a network won't help them learn non-linear computations.

## Dropout regularization

* Probability of "turning off" a given neuron of the layer
* Inverted dropout \- ensure that the activations keep the same (the ones that are activated): 
	- $d3 = np.random.randn(a3.shape[0], a3.shape[1]) < keep\_prob$
	- $a3 = np.multiply(a3, d3) $
	- $a3 = a3 / keep\_prob $
* Dropout isn't used at test time because you don't want your output to be random


## Understanding dropout

* Intuition: Can't 