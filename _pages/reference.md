---
layout: archive
title: ""
permalink: /reference/
author_profile: true
redirect_from:
  - /reference
---

{% include base_path %}

Docker
======
Basic commands when you have the 'Dockerfile' in the repository.
* <b>Build Docker</b>
    ~~~
    docker build -t <container-name> .
    ~~~
* <b>Run Docker</b>
    ~~~
    docker run -it -rm --name test --privileged <container-name>:<tag> bash
    ~~~