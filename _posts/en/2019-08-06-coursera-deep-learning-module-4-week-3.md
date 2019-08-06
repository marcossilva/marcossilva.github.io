---
layout: post
title:  "Coursera Deep Learning Module 4 Week 3 Notes"
ref: coursera-deep-learning-4-3
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-08-06T02:08:00-03:00
dateModified: 2019-08-06T02:08:00-03:00
description: Notes of the fourth Coursera module, week 3 in the deeplearning.ai specialization
image: /assets/course4.jpeg
---

{% include figure.html filename="course4" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Convolutional Neural Networks" width="50%" %}

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

## Object Localization

Image classification takes an image and classify it in a given set of classes. Classification with localization also pinpoint the bound box of the localization of the object in the image. The object detection usually works out with multiple tasks at the same time.

Localization can be taught to the network with the output parameters being set as $b_x, b_y$ for the bounding box middle point and $b_w, b_h$ for the width and height respectively. Therefore the output of the network now has 4 extra outputs which determine the position of the object in the given image. To help the learning the values are normalized using one of the corners (as the top left) as $(0,0)$ and the opposite corner as $(1,1)$.

The loss here is only calculated when an object is detected. When no object is detected we don't care for the bounding box positions calculated and those are not taken into the loss of that particular step.

## Landmark Detection

Landmark detection basically is the subset of localization where you pinpoint the localization of several points in the image at the same time, like in the Snapchat filter where it pinpoints the faces and uses that input to apply a filter.

## Object Detection

Using slide window detection you can build a ConvNet that detects a given object using a small sample of image and use a sliding window to classify over a bigger image. Given different sizes and strides of sliding windows you can detect the position of objects at the cost of high computational cost if the windows are sequentially processed.

## Convolutional Implementation of Sliding Windows

If instead of using fully connected layers you had the same filters from the last convolution but with the number of channels set to the number of neurons you would like to have in the next fully connected layer the output would be a $ 1 \times 1 \times n_c$ where $n_c = $ number of neurons you would have in the fully connected layer. Using this same technique you can follow up using $1 \times 1$ filters and setting the following $n_c$ as the number of neurons you would have in the subsequent layers until the last layer where $n_c$ would be the same size as your outputs.

Now if we had an input which is bigger than our expected network would output we could simply use this bigger input and get a bigger output which would correspond exactly to the computation of all subsamples in the given input. If our input would have been processed 4 times to fit the original input that means the output would be 4 times bigger than a single output. As the convolution operations share a lot of operations is much faster to compute all of them together than separately.


Paper: {% include link.html href="https://arxiv.org/pdf/1312.6229.pdf" title="OverFeat: Integrated Recognition, Localization and Detection using Convolutional Networks 2014 paper by Sermanet, P., Eigen, D., Zhang, X., Mathieu, M., Fergus, R., LeCunn, Y."%}

## Bounding Box Predictions

The YOLO algorithm divides the image in a given grid and classify each cell of the grid separately. If the image is divided in a $3 \times 3$ grid and the regular output had $8$ values then the new output would be a $3 \times 3 \times 8$ volume. Remember that we only care for the bounding box prediction on the cells that have been classified as some object and all the others are don't cares.

As we're now classifying inside the defined bounding cells we expect our $b_x, b_y$ values to fit inside our cells, therefore varying between $(0,0)$ and $(1,1)$ corresponding to the corners of the bounding box. The values of $b_w, b_w$ although can vary on values bigger than $1$ as the bounding box can be over the selected grid.

Paper: {% include link.html href="https://arxiv.org/pdf/1506.02640.pdf" title="You Only Look Once:Unified, Real-Time Object Detection 2016 paper by Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi"%}

## Intersection Over Union

Intersection over union is a metric to measure the performance of bounding box prediction tasks. Given the ground truth bounding box and the predicted bounding box it computes the intersection area over union of these two bounding boxes. By convention if the IoU is greater than 0.5 the bounding box is correctly being classified.

## Non-max Suppression

<https://www.coursera.org/learn/convolutional-neural-networks/lecture/dvrjH/non-max-suppression>