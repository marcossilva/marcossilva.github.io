---
layout: post
title:  My first steps on BERT
ref: bert
lang: en
categories: en
tags: deep-learning
datePublished: 2019-08-17T01:54:00-03:00
dateModified: 2019-08-17T01:54:00-03:00
description: My impressions on the steps trying to understand the NLP state of the art current models (BERT and ELMo)
---

Since I've finished my Deep Learning Course on deeplearnin.ai I've been looking for more resources on the newest state of the art (SOA) models in NLP. Much has changed since the course was deployed on Coursera but I think that with what I've already learnt I'm more than capable of understanding the new models with the available resources on the internet. In this post I'll pinpoint my understandings in the way they made sense to me and, hopefully, it helps others to blink and understand them as well.

I'm assuming you already know what word vectors are. Simply put the take a word and output a contextualization of it based on what it has learned from some corpus of text. A common corpus of text is the Wikipedia. It's taken as not biased, deals with many different aspects of human topics and it's considerably large. On the deeplearning.ai course they've already tackled the challenge that bias can be in this kind of models since it takes into account most of the time subjective bias which people may not be aware of until it becomes a problem. Word Vectors can be trained with many different approaches as word2vec, Glove and fasttext. But in their roots they commonly share the same problems. Let's take the following sentences as examples:

> Your Teddy Bear need to take a bath since you have been playing with him all day long in the dirt.
> Teddy Roosevelt was an amazing president and his face can still be seen today in Mount Rushmore.

1) Names contextualization

In the above sentences both uses Teddy as name. But in the first one depicts a plush toy and in the second one one of the USA presidents. The contextualization of the vectors in word embeddings approaches usually takes the same direction as the language it's representing. Therefore English, for example, is read from left to right. But when the word Teddy is first read it's not possible to still know if we're talking about the bear or the president. One of the aspects BERT brings is the Bidirectional approach in which it takes in consideration both directions and greatly reduces this problem as the context taken from the end of the sentence would be able to identify which Teddy is being referred to.

2) Coreference

In natural language it's not uncommon to refer a previous noun by it's pronouns. In the sentences we use his to refer to Teddy. Word Embeddings although are not able to seek in the previous words until it approaches the correct reference for that word. A solution for this problem on the BERT is the self attention model. With the self attention model either the encoder and the decoder have the opportunity to look to all the primary encodings of each word (event taking in account its bidirectionality) and apply the attention correctly on the words. Therefore in a first step the bidirectionality would take care of the problem (1) of names contextualization and the self-attention would take this generated embeddings and apply the correct contextualization. In our case, for example, that means that the 'his' on the Teddy Bear sentence would take into account the Teddy embedding that in turn already carries the meaning of the bear with it. The same happens in the second sentence: The bidirectionality takes care of solving the name contextualization and the self attention allows the coreference to be adjusted to the correct equivalent nouns it refers to.

While ELMo computes the left to right and the right to left and then compute over both separately BERT uses a Bidirectional solution.


## References:

1. <https://www.youtube.com/watch?v=BhlOGGzC0Q0>

Paper: {% include link.html href="https://arxiv.org/pdf/1409.3215" title="Sequence to Sequence Learning with Neural Networks 2015 by Ilya Sutskever, Oriol Vinyals, Quoc V. Le"%}

