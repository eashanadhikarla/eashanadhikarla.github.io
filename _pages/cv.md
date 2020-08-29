---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Download - [Resume.pdf](https://eashanadhikarla.github.io/files/Resume.pdf)

Education
======
* <b>Ph.D</b> in Machine Learning, Lehigh University, <i>Aug 2020 - May 2025 (expected)</i>
* <b>M.S.</b> in Computer Science, Lehigh University, <i>Aug 2018 - May 2020</i>
* <b>B.E.</b> in Computer Science, Rajiv Gandhi Proudyogiki Vishwavidyalaya, <i>Aug 2013 - June 2018</i>

Work experience
======
* <i>Peer Mentor</i>, National Science Foundation (NSF-REU) 2020 (<a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1757787">CNS-1757787</a>)
  * Mentoring and closely guiding 15 NSF-REU Interns on their respective site projects.
  * Duties included: Weekly one-on-one discussions with each intern, understanding their fallouts and helping them out with their codes and other low level academic issues.

* <i>Research Assistant</i>, Resilience Research Group for SARS-CoV-2 (<a href="https://converge.colorado.edu/resources/covid-19/working-groups/issues-impacts-recovery/cultural-perceptions-of-risk-behavioral-responses-and-community-resilience-in-covid-19">NSF Award 1841338</a>)
  * Image Gathering for face-masks in United States.
  * Designing a novel face-mask detection algorithm for a survey research on SARS-CoV-2.
  * Supervisor: <a href="http://www.cse.lehigh.edu/~brian/">Dr. Brian D. Davison</a>

* <i>Research Intern</i>, Lawrence Berkeley National Lab, NERSC (<a href="https://cs.lbl.gov/news-media/news/2019/summer-student-researchers-wrap-up/"><i>link</i></a>) <!-- Embedded Link: https://cdn.cp.adobe.io/content/2/video/3d0f97fc-0135-492b-b4f0-6c0d269cc2d7/embed?api_key=MarvelCP1 -->
  * Developed scripts to fetch and analyze terabytes of data from the SLURM scheduler.
  * Analyzed & estimated real-time queues in the scheduler for optimizing the policies for incoming jobs.
  * Developed three real-time policies that potentially improved the allocation procedure.
    * Draining
    * Job Cancellation
    * Job Pausing
  * Supervisor: <a href="https://www.nersc.gov/about/nersc-staff/advanced-technologies-group/brian-austin/">Dr. Brian Austin</a>

* <i>Machine Learning Intern</i>, Persistent Systems ltd (<a href="https://github.com/eashanadhikarla/Facial-Recognition-with-DNN"><i>link</i></a>)
  * Developed a facial recognition and verification system using Google's FaceNET research as the baseline.
  * Added additional OpenCV features on top of it, which can differentiate between 3-D and 2-D images.
  * Designed a purely browser-based RSA compliant module to work with FIDO keys.

Projects
========
* <b>Robust Adversarial Filter</b> (Python, PyTorch) (<a href="https://github.com/eashanadhikarla/seqGAN">link</a>)
  * Currently designing a robust auto-encoder and GAN for detecting adversarial images. Developed a close proximity approximation model which is also known as on manifold adversarial detectors. Enhanced the vanilla auto-encoder to a deep architecture with enforced learning from memory elements.

* <b>Sequence Generative Adversarial Nets with Policy Gradient</b> (Python, PyTorch) (<a href="https://github.com/eashanadhikarla/seqGAN">link</a>)
  * Seq-GAN is a unique approach which models the data generator as a stochastic policy in reinforcement learning to solve the problem.
  * The RL reward signal comes from the GAN discriminator judged on a complete sequence, and is passed back to the intermediate state- action steps using Monte Carlo search.

* <b>Facial Recognition and Verification System</b> (Python) (<a href="https://github.com/eashanadhikarla/Facial-Recognition-with-DNN"></a>)
  * Realtime recognition system focused on mobile devices.
  * Overcame the challenge of keeping a low false-positive rate by developing a unique approach learning directly from 128-D embedding into a Euclidean space.

Skills
======
* <b>Languages</b>        - Python, C, C++, Java, Bash, Scala
* <b>Framework</b>        - MySQL, HTML, NoSQL, Javascript
* <b>Tools & Lbraries</b> - Pytorch, Tensorflow, OpenCV, dlib, Boost-C++, Cmake, scikit-learn, git, Latex

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>