---
layout: post
title:  "Coursera Deep Learning Module 3 Week 2 Notes"
ref: coursera-deep-learning-3-2
lang: en
categories: en
tags: deep-learning lecture-notes coursera
datePublished: 2019-08-03T02:08:00-03:00
dateModified: 2019-08-03T02:08:00-03:00
description: Notes of the third Coursera module, week 3 in the deeplearning.ai specialization
image: /assets/Course3.png
---

{% include figure.html filename="Course3" extension="jpeg" alt="logo of deeplearning.ai neural networks course" title="Neural Network Deeplearning.ai Logo" caption="Structuring Machine Learning Projects" width="50%" %}

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

## Carrying out error analysis

Imagine your cat classifier has 90% accuracy and 10% error. From that 10% error you think it's due to wrongly classifying some dogs as cats. Should you try to make your cat classifier do better on dogs? To answer this question we must do error analysis. To achieve this analysis get 100 images on the dev set that are being mislabeled. Count up how many are dogs. Imagine for example that only 5/100 images are dogs. That means that even if you've fully solved the dog classification problem your error would only go down 5%, coming from 10% to 9.5% at best. This is the "ceiling" of your next step.

Multiple ideas can be evaluated in parallel to quickly decide which one might have bigger impact on your error reduction process.

## Cleaning up incorrectly labeled data

DL algorithms are quite robust to random errors but much less robust to systematic errors. The incorrectly labeled data impact can be analyzed as any other error analysis metric with the same estimation on the resulting impact.

## Build your first system quickly, then iterate

