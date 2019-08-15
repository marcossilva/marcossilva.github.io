---
layout: post
title:  "Coursera Deep Learning Module 1 Week 4 Notes"
ref: coursera-deep-learning-1-4
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-06-24T02:25:00-03:00
dateModified: 2019-07-01T23:21:00-03:00
description: Notes of the first Coursera module, week 4 in the deeplearning.ai specialization
image: /assets/Course1-1.png
---

{% include figure.html filename="Course1-1" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Neural Networks" width="50%" %}
{% include prevnext.html prev="/en/2019/06/24/coursera-deep-learning-notes-module-1-week-3.html" next="/en/2019/07/03/coursera-deep-learning-module-2-week-1.html" %}
## Week 4
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

## Parameter vs Hyperparameter

* Parameters:
	* Weights
	* Biases
* Hyperparameters: 
	* Learning rate $\alpha$ or $f(t) = \theta $
	* \# iterations
	* \# hidden units
	* choice of activation function
	* Momentum
	* Mini-batch size
	* Regularization

## Quiz

1. What is the "cache" used for in our implementation of forward propagation and backward propagation?
	* [ ] We use it to pass variables computed during backward propagation to the corresponding forward propagation step. It contains useful values for forward propagation to compute activations.
	* [X] We use it to pass variables computed during forward propagation to the corresponding backward propagation step. It contains useful values for backward propagation to compute derivatives.
	* [ ] It is used to keep track of the hyperparameters that we are searching over, to speed up computation.
	* [ ] It is used to cache the intermediate values of the cost function during training.

2. Among the following, which ones are "hyperparameters"? (Check all that apply.)
	* [ ] activation values $a^{[l]}$
	* [X] number of iterations
	* [ ] weight matrices $W^{[l]}$
	* [X] number of layers $L$ in the neural network
	* [X] learning rate $\alpha$
	* [X] size of the hidden layers $n^{[l]}$
	* [ ] bias vectors $b^{[l]}$

3. Which of the following statements is true?
	* [X] The deeper layers of a neural network are typically computing more complex features of the input than the earlier layers
	* [ ] The earlier layers of a neural network are typically computing more complex features of the input than the deeper layers

4. Vectorization allows you to compute forward propagation in an LL-layer neural network without an explicit for-loop (or any other explicit iterative loop) over the layers l=1, 2, …,L. True/False?
	* [ ] True
	* [X] False

5. Assume we store the values for n^{[l]} in an array called layers, as follows: layer_dims = [n_x,4,3,2,1]. So layer 1 has four hidden units, layer 2 has 3 hidden units and so on. Which of the following for-loops will allow you to initialize the parameters for the model?
	* [ ] ```python
			for(i in range(1, len(layer_dims)/2)):
		  parameter[‘W’ + str(i)] = np.random.randn(layers[i], layers[i-1])) * 0.01
		  parameter[‘b’ + str(i)] = np.random.randn(layers[i], 1) * 0.01
		  ```
	* [ ] ```python
			for(i in range(1, len(layer_dims)/2)):
		  parameter[‘W’ + str(i)] = np.random.randn(layers[i], layers[i-1])) * 0.01
		  parameter[‘b’ + str(i)] = np.random.randn(layers[i-1], 1) * 0.01
		  ```
	* [ ] ```python
			for(i in range(1, len(layer_dims))):
		  parameter[‘W’ + str(i)] = np.random.randn(layers[i-1], layers[i])) * 0.01
		  parameter[‘b’ + str(i)] = np.random.randn(layers[i], 1) * 0.01
		  ```
	* [X] ```python
			for(i in range(1, len(layer_dims))):
		  parameter[‘W’ + str(i)] = np.random.randn(layers[i], layers[i-1])) * 0.01
		  parameter[‘b’ + str(i)] = np.random.randn(layers[i], 1) * 0.01
		  ```

6. Consider the following neural network. How many layers does this network have?
	* [X] The number of layers L is 4. The number of hidden layers is 3.
	* [ ] The number of layers L is 3. The number of hidden layers is 3.
	* [ ] The number of layers L is 4. The number of hidden layers is 4.
	* [ ] The number of layers L is 5. The number of hidden layers is 4.

7. During forward propagation, in the forward function for a layer l you need to know what is the activation function in a layer (Sigmoid, tanh, ReLU, etc.). During backpropagation, the corresponding backward function also needs to know what is the activation function for layer l, since the gradient depends on it. True/False?
	* [X] True
	* [ ] False

8. There are certain functions with the following properties: (i) To compute the function using a shallow network circuit, you will need a large network (where we measure size by the number of logic gates in the network), but (ii) To compute it using a deep network circuit, you need only an exponentially smaller network. True/False?
	* [X] True
	* [ ] False

9. Consider the following 2 hidden layer neural network:
Which of the following statements are True? (Check all that apply).
	* [X] $W^{[1]}$ will have shape (4, 4)
	* [X] $b^{[1]}$ will have shape (4, 1)
	* [ ] $W^{[1]}$ will have shape (3, 4)
	* [ ] $b^{[1]}$ will have shape (3, 1)
	* [X] $W^{[2]}$ will have shape (3, 4)
	* [ ] $b^{[2]}$ will have shape (1, 1)
	* [ ] $W^{[2]}$ will have shape (3, 1)
	* [X] $b^{[2]}$ will have shape (3, 1)
	* [X] $W^{[3]}$ will have shape (3, 1)
	* [X] $b^{[3]}$ will have shape (1, 1)
	* [ ] $W^{[3]}$ will have shape (1, 3)
	* [ ] $b^{[3]}$ will have shape (3, 1)

10. Whereas the previous question used a specific network, in the general case what is the dimension of W^{[l]}, the weight matrix associated with layer ll?
	* [ ] $W^{[l]}$ has shape $(n^{[l-1]}, n^{[l]})$
	* [X] $W^{[l]}$ has shape $(n^{[l]}, n^{[l-1]})$
	* [ ] $W^{[l]}$ has shape $(n^{[l]}, n^{[l+1]})$
	* [ ] $W^{[l]}$ has shape $(n^{[l+1]}, n^{[l]})$

{% include prevnext.html prev="/en/2019/06/24/coursera-deep-learning-notes-module-1-week-3.html" next="/en/2019/07/03/coursera-deep-learning-module-2-week-1.html" %}