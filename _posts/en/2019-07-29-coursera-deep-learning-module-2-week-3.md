---
layout: post
title:  "Coursera Deep Learning Module 2 Week 3 Notes"
ref: coursera-deep-learning-2-3
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-07-29T02:08:00-03:00
dateModified: 2019-07-29T02:08:00-03:00
description: Notes of the second Coursera module, week 3 in the deeplearning.ai specialization
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
<style type="text/css">
	div.code-highlited-mod{font-family:monospace;font-size: 15px;border: 1px solid #e8e8e8;border-radius: 3px;background-color: #eef;padding: 8px 12px;overflow-x: auto;}
</style>

## Hyperparameter Tuning
1. Alpha (Learning Rate)
2. Mini-batch Size, Beta (momentum), #hidden units
3. #layers, learning rate decay
4. Adam parameters

* When sampling hyperparameters to select the best don't use a grid system. As it might seem intuitive in the end it reduces the search space intuition of which parameter affects the metrics mre or less. Randomly selecting values in a range can provide much better variation and perception on which one is more important and how that one (or event the combination) varies on the selected range.
* Coarse to fine scheme: given an initial coarse sampling and a focused area of interest we can increase the sampling in that specific area.

## Using an appropriate scale to pick hyperparameters

* number of layers, number of neurons in a given layer -> Good examples of randomly linear sampling working well
* learning rate, exponentially weighted averages betas -> better with logscale since in the linear scale much more resources would be spent on bigger variations than smaller variations. $r = -4 * np.random.rand()$, $alpha = 10^r$

## Hyperparameters tuning in practice: Pandas vs. Caviar
* There might be cross information in other application domains
* As everything else changes (data, model, etc) the hyperparameters might change as well
* Babysitting model (Panda) x Parallel models (aCviar) -> It's about resources. If you don't have resources you focus everything you have on that model; if you have many resources available simply train them all.

## Normalizing activations in a network

* Can we normalize $a^{[l]}$ to train $W^{[l+1]}, b^{[l+1]}$ faster? Instead of using $a^{[l]}$ is more common to use $Z^{[l]}$

<div class="code-highlited-mod">
	<p>Given some intermediate values in NN $z^{(1)} ... z^{(n)} = Z^{[l](i)}$</p>
	<p>$\mu = \frac{1}{m} \sum_i{z^{(i)}}$</p>
	<p>$\sigma^2 = \frac{1}{m} \sum_i{z_i - \mu}^2$</p>
	<p>$z^{(i)}_{norm} = \frac{z^{(i)} - \mu}{\sqrt{\sigma^2 + \varepsilon}}$</p>
	<p>$\widetilde{z}^{(i)} = \gamma z^{(i)} + \beta$ where $\gamma$ and $\beta$ are learnable parameters</p>
</div>

* The $\gamma$ and $\beta$ values allow the batch to model any kind of distribution necessary to model and redistribute the data

## Fitting Batch Norm into a neural network
* The Batch Norm (BN) step takes place between the computation of $Z$ and $a$
* As we're changing the distribution adding any bias value has no meaning. The BN turn the mean to 0 and therefore has no reason to add any bias

<div class="code-highlited-mod">
	<p>for $t=1 ... num_{mini-batches}$:
		<p style="text-indent: 2em;">Compute forward-propagation on $X^{\{t\}}$</p>
		<p style="text-indent: 2em;">In each hidden layer use BN to replace $z^{(l)}$ to $\widetilde{z}^{(i)}$</p>
		<p style="text-indent: 2em;">Use backpropagation to compute the gradients</p>
		<p style="text-indent: 2em;">Update the weights</p>
	</p>
</div>

<https://www.coursera.org/learn/deep-neural-network/lecture/81oTm/why-does-batch-norm-work>