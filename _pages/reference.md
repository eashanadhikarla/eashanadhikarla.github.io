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
Build Docker
~~~
docker build -t <container-name> .
~~~
* <b>Run Docker</b>
    ~~~
    docker run -it -rm --name test --privileged <container-name>:<tag> bash
    ~~~

Python Virtual Environment
======
On maxOS and Linux:
~~~
python3 -m venv <path-to-env/env-name>
source env/bin/activate # To activate the environment
deactivate # To deactivate the environment
~~~

Conda
======


