---
layout: post
title:  "Coursera Deep Learning Module 1 Week 2 Notes"
ref: coursera-deep-learning-1-2
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-06-21T19:00:00-03:00
dateModified: 2019-06-21T19:00:00-03:00
description: Notes of the first Coursera module, week 2 in the deeplearning.ai specialization
image: /assets/Course1-1.png
published: false
---

{% include figure.html filename="Course1-1" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Week 2 - Neural Networks Basics" width="50%" %}

## Week 2 - Neural Networks Basics

### Binary Classification
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
Given a pair $$(x, y)$$ where $$x \in \mathbb{R}^{n_x}, y \in \{0, 1\} $$. With $$m$$ training examples you would have $$ \{(x^1, y^1), (x^2, y^2),...(x^m, y^m)\}$$. Stacking them together you would come up with the matrices X and Y below which are much easier to train in batches since there are many vectorized optimizations readily available. $$X \in \mathbb{R}^{n_x \times m}, Y \in \mathbb{R}^{1 \times m} $$

### Logistic Regression

* Given $x$ we want the $ \hat{y} = P(y=1 \| x) $
* $x \in \mathbb{R}^{n_x}, 0 \geq \hat{y} \geq 1$
* Parameters: $ w \in \mathbb{R}^{n_x}, b \in \mathbb{R} $
* Output $\hat{y} = \sigma(w^Tx + b)$
* $z = w^Tx + b$
* $\sigma(z) = \frac{1}{1+e^{-z}}$
* If z is large ($$\displaystyle\lim_{z\to\infty}$$) then $\sigma(z) \approx \frac{1}{1+0} = 1$
* If z is a large negative number ($$\displaystyle\lim_{z\to-\infty}$$) then $\sigma(z) \approx \frac{1}{1+\infty} \approx 0$

### Logistic Regression Cost Function

* Given $$ \{(x^1, y^1), (x^2, y^2),...(x^m, y^m)\}$$, we want $ \hat{y}^{(i)} \approx y^{(i)}$
* Squared Error: $\mathcal{L}(\hat{y}, y) = \frac{(\hat{y} - y)^2}{2}$ might not be a good option because it's not convex
* $\mathcal{L}(\hat{y}, y) = (y\log\hat{y} + (1-y)\log(1-\hat{y}))$
* If $y=1: \mathcal{L}(\hat{y}, y) = -\log\hat{y}$ <- want $\log\hat{y}$ to be large meaning we want $\hat{y}$ large
* If $y=0: \mathcal{L}(\hat{y}, y) = -\log\(1-hat{y})$ <- want $\log(1-\hat{y})$ to be large meaning we want $\hat{y}$ small
* **Cost function**: $\mathcal{J}(w, b) = \frac{1}{m} \sum_{i=1}^{m}\mathcal{L}(\hat{y}^{(i)}, y^{(i)})$, in other words, the cost function is the average of the loss on the given examples
* Loss function applies to a single training example
* Cost function applies to all the examples

### Gradient Descent

* We want to find $w, b$ that minimize $\mathcal{J}(w, b)$
* This loss function is convex, therefore pointing to a single minima
* Gradient Descent: $w := w - \alpha \frac{\partial\mathcal{J}(w, b)}{\partial w}$ and $b := b - \alpha \frac{\partial\mathcal{J}(w, b)}{\partial b}$ where $\alpha$ is the learning rate

### Derivatives

* Intuition about derivatives: $f(a) = 3a$ the slope of $f(a)$ at $a=2$ is 3 and at $a=5$ is 3 as well. Therefore $\frac{df(a)}{da} = 3 = \frac{d}{da}f(a)$
* In a line the slope doesn't change, therefore the derivative is constant

### More Derivative Examples

* $f(a) = a^2$ the slope of $f(a)$ at $a=2$ is 4 and at $a=5$ is 10. Therefore $\frac{df(a)}{da} = 2a $
* The slope is different for different values asi t doesn't increases linearly.
* $f(a) = a^3$ has derivative as $\frac{df(a)}{da} = 3a^2 $
* $f(a) = \ln(a)$ has derivative as $\frac{df(a)}{da} = \frac{1}{a} $
* The derivative means the slope of the function
* The slope of the function can be different on different points of the function

### Computation Graph

* $\mathcal{J} = 3(a+bc)$
* $ u = bc$
* $ v = a+u$
* $\mathcal{J} = 3v$
* One step of backward propagation on a computation graph yields derivative of final output variable.

### Derivatives with a Computation Graph

* $\frac{d\mathcal{J}}{dv} = 3$
* $$ \frac{d\mathcal{J}}{da} = \frac{d\mathcal{J}}{dv} \frac{dv}{da} = 3 * 1 = 3 $$ (chain rule)
* $\frac{d\mathcal{J}}{du} = \frac{d\mathcal{J}}{dv} \frac{dv}{du} = 3 * 1 = 3$ (chain rule)
* $\frac{d\mathcal{J}}{db} = \frac{d\mathcal{J}}{du} \frac{du}{db} = 3 * 2 = 6$ (chain rule)
* $\frac{d\mathcal{J}}{db} = \frac{d\mathcal{J}}{du} \frac{du}{dc} = 3 * 3 = 9$ (chain rule)
* The best way is to flow from the right to left
* In this class, what does the coding convention dvar represent?
	- [ ] The derivative of any variable used in the code.
	- [ ] The derivative of input variables with respect to various intermediate quantities.
	- [X] The derivative of a final output variable with respect to various intermediate quantities.

### Logistic Regression Gradient Descent

* Suppose we only have two features $$x_1$$ and $$x_2$$