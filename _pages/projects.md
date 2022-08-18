---
title:
permalink: /projects/
author_profile: true
---

<style>
hr { 
  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: 40em;
  border-style: inset;
  border-width: 2px;
}
</style>

<hr>

Research Projects
======

### Attack Framework for Randomized Input Sampling Explanation for Black Box Models (Python, PyTorch) CURRENT PROJECT** <!-- (<a href="https://github.com/eashanadhikarla/">link</a>) -->
RISE is a Explainable AI framework for deep neural networks that take images as input and output a class probability. Here, RISE generates an importance map indicating how salient each pixel is for the model’s prediction.
  * We designed a novel GAN framework to break RISE and prove that it is not as robust.
  <!-- * We would also expand the framework from Image Classification task to Object Detection task (D-RISE). -->

### Memory Defense: More Robust Classification via a Memory-Masking Autoencoder (Python, PyTorch, Advertorch) (<a href="https://github.com/eashanadhikarla/">link</a>)
  * We developed a robust autoencoder with one-hot memory masking to mitigate adversarial attacks.
  * The proximity approximation model can retrieve an image's relevant memory features and reconstruct it with a repaired label.
  * The enhanced deep neural architecture significantly improved the robustness of DNN for an image classification task.

### Face-Mask Detection on real-world Webcam dataset (Python, Bash, ffmpeg, Pytorch, COCO Annotator)
  * Successfully collected more than 1000 Gb of public webcam data, by capturing image frames periodically from over 75 webcams across United States.
  * Applied Coco-annotation semi-automated labelling to develop ground-truth labels.
  * Re-implemented 13 state-of-the-art face detection algorithms for face detection & face mask detection to analyze their effectiveness in real-world dataset.
  * Reported face mask usage across United States from Jun' 2020 to Mar' 2021.

### Sequence Generative Adversarial Nets with Policy Gradient (Python, PyTorch) (<a href="https://github.com/eashanadhikarla/seqGAN">link</a>)
  * Seq-GAN is a unique approach which models the data generator as a stochastic policy in reinforcement learning to solve the problem.
  * The RL reward signal comes from the GAN discriminator judged on a complete sequence, and is passed back to the intermediate state- action steps using Monte Carlo search.

### Facial Recognition and Verification System (Python) (<a href="https://github.com/eashanadhikarla/Facial-Recognition-with-DNN">link</a>)
  * Realtime recognition system focused on mobile devices.
  * Overcame the challenge of keeping a low false-positive rate by developing a unique approach learning directly from 128-D embedding into a Euclidean space.

<br>
<hr>

Academic Projects
======
### Image & Text Annotation using Reinforcement Learning (Python) (<a href=" https://github.com/eashanadhikarla/Image-Text-Annotation-Using-Reinforcement-Learning">link</a>)
  * In this team project, I build a deep learning model using Inception V3 as my base to extract features from the images and to pass on the feature array vector to the text annotation model in whole to generate a multi-arm bandit algorithm with a challenge of very little labelled data.

### Predicting the attractiveness of the list of products on Amazon (Python) (<a href="https://github.com/eashanadhikarla/product_listing_attractiveness">link</a>)
  * The quality of product listing is crucial for improving search relevance and gaining customer attention. I had implemented a neural network model with the help of keras text processing to learn the amazon dataset after feature engineering and cleaning the data. 

### Two-Phase Commit Replicated Hash Table (C++, Bash, Amazon EC2) (<a href="https://github.com/eashanadhikarla/Atomic-Commit-Protocol-2PC">link</a>)
  * Implemented a hash table which ensures distributed atomic transactions in the system. It replicates every operation as backup on separate node for recovery phase.

### Twitter Trend Analysis of data to create high frequency contextual word (C++, MongoDB, HTML5) (<a href="https://github.com/eashanadhikarla/Twitter-Trend-Analyzer">link</a>)
  * Using twitter data to do analysis and extract the most frequently used dictionary for political campaign. This application has been been implemented in C++ and MongoDB back-end.