---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
<!-- Download - [Resume.pdf](https://eashanadhikarla.github.io/files/resume.pdf) -->

Education
======
* <b>Ph.D.</b> in Computer Science, Lehigh University, Aug 2020 - May 2025 (expected)
  * Doctor of philosophy: I enable machines that can expand their visual knowledge by interacting with and learning directly from people.
  * Advisor:  <a href="http://www.cse.lehigh.edu/~brian/">Dr. Brian D. Davison</a>
  * Focus area: Data Science, Machine Learning, Computer Vision
* <b>M.S.</b> in Computer Science, Lehigh University, Aug 2018 - May 2020
  * Advisor: <a href="http://www.cse.lehigh.edu/~brian/">Dr. Brian D. Davison</a>, <a href="http://www.cse.lehigh.edu/~sxie/">Dr. Xie Sihong</a>
  * Focus area: Artificial Intelligence (A.I.)
* <b>B.E.</b> in Computer Science, Rajiv Gandhi Proudyogiki Vishwavidyalaya, Aug 2013 - June 2017

Work experience
======
* Ph.D. Summer Intern, <b>Lawrence Berkeley National Lab, ESnet</b>
  * Supervisor: <a href="https://cs.lbl.gov/about/staff/leadership/inder-monga/">Dr. Inder Monga</a>, Mentor: <a href="https://www.es.net/about/esnet-staff/advanced-network-technologies/ezra/">Dr. Ezra Kissel</a>

* Peer Mentor, <b>Lehigh University (NSF-REU) 2020</b> (<a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1757787">CNS-1757787</a>)
  * Mentoring and closely guiding 15 NSF-REU Interns on their respective site projects.
  * Duties included: Weekly one-on-one discussions with each intern, understanding their fallouts and helping them out with their codes and other low level academic issues.

* Research Assistant, <b>Resilience Research Group for SARS-CoV-2</b>
  * Supervisor: <a href="http://www.cse.lehigh.edu/~brian/">Dr. Brian D. Davison</a>
  * Image Gathering for face-masks in United States.
  * Designing a novel face-mask detection algorithm for a survey research on SARS-CoV-2.
  * Funded by Lehigh Research Grants and partially funded by (<a href="https://converge.colorado.edu/resources/covid-19/working-groups/issues-impacts-recovery/cultural-perceptions-of-risk-behavioral-responses-and-community-resilience-in-covid-19">NSF-1841338</a>)

* Research Intern, <b>Lawrence Berkeley National Lab, NERSC</b> (<a href="https://cs.lbl.gov/news-media/news/2019/summer-student-researchers-wrap-up/"><i>link</i></a>) <!-- Embedded Link: https://cdn.cp.adobe.io/content/2/video/3d0f97fc-0135-492b-b4f0-6c0d269cc2d7/embed?api_key=MarvelCP1 -->
  * Supervisor: <a href="https://www.nersc.gov/about/nersc-staff/advanced-technologies-group/brian-austin/">Dr. Brian Austin</a>
  * Developed scripts to fetch and analyze terabytes of data from the SLURM scheduler.
  * Analyzed & estimated real-time queues in the scheduler for optimizing the policies for incoming jobs.
  * Developed three real-time policies that potentially improved the allocation procedure.
    * Draining
    * Job Cancellation
    * Job Pausing

* Machine Learning Intern, <b>Persistent Systems ltd</b> (<a href="https://github.com/eashanadhikarla/Facial-Recognition-with-DNN"><i>link</i></a>)
  * Developed a facial recognition and verification system using Google's FaceNET research as the baseline.
  * Added additional OpenCV features on top of it, which can differentiate between 3-D and 2-D images.
  * Designed a purely browser-based RSA compliant module to work with FIDO keys.

Projects
========
* <b>Memory Defense: More Robust Classification via a Memory-Masking Autoencoder</b> (Python, PyTorch, Advertorch) (<a href="https://github.com/eashanadhikarla/">link</a>)
  * We developed a robust autoencoder with one-hot memory masking to mitigate adversarial attacks.
  * The proximity approximation model can retrieve an image's relevant memory features and reconstruct it with a repaired label.
  * The enhanced deep neural architecture significantly improved the robustness of DNN for an image classification task.

* <b>Face-Mask Detection on real-world Webcam dataset</b> (Python, Bash, ffmpeg, Pytorch, COCO Annotator)
  * Successfully collected more than 1000 Gb of public webcam data, by capturing image frames periodically from over 75 webcams across United States.
  * Applied Coco-annotation semi-automated labelling to develop ground-truth labels.
  * Re-implemented 13 state-of-the-art face detection algorithms for face detection & face mask detection to analyze their effectiveness in real-world dataset.
  * Reported face mask usage across United States from Jun' 2020 to Mar' 2021.

* <b>Sequence Generative Adversarial Nets with Policy Gradient</b> (Python, PyTorch) (<a href="https://github.com/eashanadhikarla/seqGAN">link</a>)
  * Seq-GAN is a unique approach which models the data generator as a stochastic policy in reinforcement learning to solve the problem.
  * The RL reward signal comes from the GAN discriminator judged on a complete sequence, and is passed back to the intermediate state- action steps using Monte Carlo search.

* <b>Facial Recognition and Verification System</b> (Python) (<a href="https://github.com/eashanadhikarla/Facial-Recognition-with-DNN">link</a>)
  * Realtime recognition system focused on mobile devices.
  * Overcame the challenge of keeping a low false-positive rate by developing a unique approach learning directly from 128-D embedding into a Euclidean space.

Small Academic Projects
======
* <b>Image & Text Annotation using Reinforcement Learning</b> (Python) (<a href=" https://github.com/eashanadhikarla/Image-Text-Annotation-Using-Reinforcement-Learning">link</a>)
  * In this team project, I build a deep learning model using Inception V3 as my base to extract features from the images and to pass on the feature array vector to the text annotation model in whole to generate a multi-arm bandit algorithm with a challenge of very little labelled data.

* <b>Predicting the attractiveness of the list of products on Amazon</b> (Python) (<a href="https://github.com/eashanadhikarla/product_listing_attractiveness">link</a>)
  * The quality of product listing is crucial for improving search relevance and gaining customer attention. I had implemented a neural network model with the help of keras text processing to learn the amazon dataset after feature engineering and cleaning the data. 

* <b>Two-Phase Commit Replicated Hash Table</b> (C++, Bash, Amazon EC2) (<a href="https://github.com/eashanadhikarla/Atomic-Commit-Protocol-2PC">link</a>)
  * Implemented a hash table which ensures distributed atomic transactions in the system. It replicates every operation as backup on separate node for recovery phase.

* <b>Twitter Trend Analysis of data to create high frequency contextual word</b> (C++, MongoDB, HTML5) (<a href="https://github.com/eashanadhikarla/Twitter-Trend-Analyzer">link</a>)
  * Using twitter data to do analysis and extract the most frequently used dictionary for political campaign. This application has been been implemented in C++ and MongoDB back-end.

Skills
======
* <b>Languages</b>        - Python, C++, Bash, Scala
* <b>Framework</b>        - MySQL, HTML, NoSQL, Javascript, Apache Spark
* <b>Tools & Lbraries</b> - Pytorch, Tensorflow, OpenCV, dlib, Boost-C++, Cmake, scikit-learn, git, Latex, Pyspark

Achievements and Honors
======
* PC Rossin Fellowship, Lehigh University (Spring 2021)
* Awarded by Cognizant, for the <b>Outstanding Project Award</b> in Facial Recognition with Deep Neural Network (2016-17) 
* <b>Best Project Award</b> by the Department of Computer Science in RGPV university for ’Physical Intrusion Detection System’ (2015-16) 
* Ranked among <b>top 1 percentile</b> in TESTimony’16 organised by Tata Consultancy Services. (2015) 
* Awarded by H.C.Verma (Experimental Physicist): Winner of the <b>National Level SCEECS’16</b>: Quiz Competition organised by National Institute of Technology, Bhopal (MANIT). (2015) 
* Awarded a Trophy from <b>Central Board of Secondary Education</b> (CBSE) for performance in English subject (2013)
* Presented a Abstract Paper on Shell-shock Vulnerability at <b>National level technical symposium</b> in Bhopal: Which explained about how the attack vector works, the risks involved and how to mitigate them. This explanation of the Shell-Shock CVE was published in the National conference Magazine published by LNCT Group of College Bhopal. (2014)
* <b>All India Rank 598</b> in International Maths-Science Olympiads (2007) 

Certifications
======
* Deep Learning School for Science at <b>Lawrence Berkeley National Laboratory</b>, (2019, 2020)
* Introduction in Data Structure Programming: <b>IIT Madras - NPTEL National Programme on Technology Enhanced Learning</b>
* Linux FoundationX: edX - 93%  <a href="https://verify.edx.org/cert/3e017788d8214d68831eb2b76e6ea699">Verify</a>
* Introduction to Programming Using Python: <b>Massachusetts Institute of Technology (MIT)</b><a href="https://verify.edx.org/cert/e0d7c1ef5a084f37a95c094e2b056457">Verify</a> 
* Introduction to C++: <b>Microsoft</b> - 98% <a href="https://courses.edx.org/certificates/a63e9a2057e44639a4f03aba08fd7a04">Verify</a> 

Coursework
======
Computer Vision, Media Forensics, Adversarial Machine Learning, Big Data Analytics, Advance Programming Techniques, Introduction to Data Mining, Machine Learning MOOC, Introduction to Artificial Intelligence, Analysis and Algorithm Design, Data Structures, Object Or Computation, Discrete Mathematics, Computer System Organization, Database Management System, Computer Graphics and Multimedia, Computer Network, Software Engineering, Compiler Design, Soft-Computing.

Co-curricular
======
* Vice President of Lehigh University Crytography Club.
* Updated the school’s 10 Year standing record in Triple-Jump in session 2012-2013. 
* Won first-prize in JSSC Basket-ball Tournament.
* Won first-prize in 200 mtr Inter-district Athletics’s meet.

<!-- Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->
  
<!-- Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->