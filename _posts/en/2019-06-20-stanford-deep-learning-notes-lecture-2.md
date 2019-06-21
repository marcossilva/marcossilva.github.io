---
layout: post
title:  "Deep Learning Lecture 2 Notes"
ref: deep-learning-lecture-2
lang: en
categories: 
tags: deep-learning lecture-notes
datePublished: 2019-06-20T23:00:00-03:00
dateModified: 2019-06-20T23:00:00-03:00
description: Notes of the second Stanford deep learning course lecture.
image: /assets/learning-process.png
---

Machine Learning can be taught as learning an approximate function that maps an **input** to a desired **output**. This can be done using an **model**. The model is basically a given **architecture** and its **parameters**. The **loss** function gives you how much you should move your parameters in the given architecture to minimize your error using a gradient.

All these bolded pointed things can change in a Machine Learning problem. Apart from all those you could also change the **activation functions** used, the **optimizer** and many **hyperparameters**.

<figure>
	<p align="center">
		<picture align="center">
		  <source srcset="/assets/learning-process.webp" type="image/webp">
		  <source srcset="/assets/learning-process.png" type="image/png"> 
		  <img src="/assets/learning-process.png" title="Learning Process on Machine Learning" alt="specific things you could change in a machine learning pipeline" align="center">
		</picture>
	</p>
	<p align="center"><figcaption align="center">Things you could change and wrangle in a machine learning problem</figcaption></p>
</figure>

* Logistic Regression with single output (<a href="https://youtu.be/AwQHqWyHRpU?t=295" rel="nofollow">5:00</a>)
* Logistic Regression with multiple output (<a href="https://youtu.be/AwQHqWyHRpU?t=341" rel="nofollow">5:40</a>)
* Labeling data for multi class problems is important (<a href="https://youtu.be/AwQHqWyHRpU?t=382" rel='nofollow'>6:22</a>)
	* One-hot encoding - A vector with only one value marked as one and all the others as zero. Can lead to really sparse vectors. Works very well with a single classification and not multi classification in the given input.
	* Label encoding - Numerical encoding to the input. Turn the input into sequential data
* Shallow network 'understanding' of the input given different depth (<a href="https://youtu.be/AwQHqWyHRpU?t=615" rel='nofollow'>10:15</a>)

## Day 'n' Night Detector(<a href="https://youtu.be/AwQHqWyHRpU?t=763" rel='nofollow'>12:40</a>)
- Classify if a given image is a day image or a night image
- How decide how many images? 
	- 1st rule of thumb: use complexity. Complex tasks need more data. 
	- 2nd rule of thumb: use experience given the data you'll have available
- How divide images into train/test/validation test sets? 80/10/10?
- Bias? We should be careful to give our model a balanced dataset to mitigate problems. There are specific techniques to deal with unbalanced data.
- How choose resolution of the input image?
	- Compare to human performance. Print many resolutions and give to humans and establish a baseline performance for each resolution

## Face Verification (<a href="https://youtu.be/AwQHqWyHRpU?t=1343">22:23</a>)
- Validate student IDs to a camera captured image
- How big the images should be? Over 400px preferably. Why? Because the task is much more complex than the previous one. 
- Architecture: Siamese Network? Both inputs are encoded using a network and both encodings are subtracted.
- Loss function should focus on triplets: the available correct pair to be minimized and a incorrect pair. It's also important to note that there is an alpha term in the loss because it avoids learning the mapping to 0 which would lead to no error (and no learning at all)

## Face Recognition (<a href="https://youtu.be/AwQHqWyHRpU?t=2577">42:55</a>)
- There's no validation anymore. The camera identifies you.
- Face Recognition: K-Nearest Neighbors
- Face Clustering: K-Means
- Maybe we need to detect the face first? Another separated module.

## Art Generation (<a href="https://youtu.be/AwQHqWyHRpU?t=2915">48:35</a>)
- Given a picture, make it look beautiful
- Which data? Beautiful is a super personal and fluid concept. The input data can be, therefore, any image
- The **input** can be a pair of images with a given image that we want to apply the style and a given image that we want to extract the style from.
- The **output** we want is a generated image
- The model is a style-network. We want a model that is not restricted to a specific style but is able to extract style from any image content.
- Gram Matrix. Style is non-localized information.
- The loss function wants to maximize both terms: the style and the content.
- The downsize of a model that can output **any** style is that for each image generated it's necessary to run the image multiple times until the loss is small enough given the number of iterations. Another approach would be a network that output a given style. This approach would be much faster to output a single style but wouldn't be able to generate multiple styles.
- The approach to multiple styles would be feed a random noise as input and compute the loss until it is small enough meaning that both content and style have been correctly transfered.

## Trigger Word Detection (<a href="https://youtu.be/AwQHqWyHRpU?t=3807">1:03:27</a>)
- Given a 10s audio speech, detect the word 'activate'
- 'Resolution' (Sampling rate) of audio? the best way to decide this is with human baseline like the images test.
- Labeling schema for time steps x for whole audio. Using a single output is much harder for the algorithm because much of the input is actually not the word being detected. The timestep labeling is much easier but generates an unbalanced dataset. A hack to balance it back is to map not just the time step with the word being detected but its neighbors as well.
- Strategic data collection:
	- Manual data collection
	- Manual labeling
	- Movie subtitles
	- Audio books
	- Automatic labeling + Programmatically. Generating samples strategy:
		- Data:
			- Background Noise
			- Positive Samples
			- Negative Samples
		- Technique:
			- Mix the 3 datasets randomly in a known labeled way
			- Mixing them randomly augment the dataset easily generating thousands of samples pretty easily, on-the-fly and doesn't even require a large database of any of the samples
- Input data -> Fourier Transform (FFT) -> LSTM
- FFT itself has its own hyperparameters
- A better approach: Input data -> Fourier Transform (FFT) (v2 Hyperparameters) -> Conv + BatchNorm (BN) -> GRU + BN -> Activation -> Expanded Output