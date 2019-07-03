---
layout: post
title:  "Deep Learning Lecture 3 Notes"
ref: deep-learning-lecture-3
lang: en
categories: en
tags: deep-learning lecture-notes
datePublished: 2019-07-02T23:00:00-03:00
dateModified: 2019-07-02T23:00:00-03:00
description: Notes of the third Stanford deep learning course lecture.
image: /assets/stanford-logo.png
---
{% include figure.html filename='stanford-logo' extension='png' alt='Block S (One color in Red on a Dark Background)' title='Stanford Logo' caption='Stanford Logo' width='20%' %}

{% include link.html href='https://youtu.be/JUJNGv_sb4Y' text='Youtube Recording' %}

## Full cycle machine learning

Steps of an ML project/application:

1. Select a problem (Supervised Learning) 
	- Voice Activated Device
	- X (audio) -> y (wake word)
2.  Get data
3. Design model
4. Train model
5. Test model
6. Deploy
7. Maintain
8. Quality Assurance

I. What are good projects to work on machine learning?
Voice activated devices are good in theory but pretty bad to interact and the wifi setup is painfully hard.

* Domain knowledge
* Data availability
* Money
* Utility
* Feasibility

II. Data collection.

* How many days would you spend collecting data?
* How would you collect data?
* Rather than spending much time collecting data try to rapidly collect an initial data to start the training phase

III. Design model

* Keep clear notes on experiments run to ease the comparation and the outputs metrics tracking

VI. Deploy

* Edge devices where the model is served have much less computational processing than high end devices in which the model is usually trained
*  A system may be inserted before the main processing system which could be simpler as a volume threshold or a simpler network. A volume threshold would be super simple to implement easily and manually adapt which strongly helps out the debugging. A simpler network could also be quickly trained but probably not as quickly although the final output could be much better.
* Most of the time the trained data is not the same as the data the model has to perform well (data changes). The data could also change from data source to data source (as changing from an high end microphone to and low end version to collecting voice)
* A non-ML approach could probably be more robust to the data change as it is not learned from data but simply inserted as specialized knowledge. Sometimes this handwritten rule can be hard to implement if the task is hard but simple starting filters can highly improve the performance and robustness of the model
* Does a cloud edge deployment model make maintenance easier, and why? It's easier to push updates, easier to collect the user data to a single server

<a href="{{ site.baseurl }}{% link _posts/en/2019-05-20-stanford-deep-learning-notes-lecture-index.md  %}">Classes Index</a>