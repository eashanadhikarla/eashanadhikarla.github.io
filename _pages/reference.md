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
<!-- <embed src="files/conda-cheatsheet.pdf" type="application/pdf" width="100%" height="600px" /> -->
<!-- <embed src="files/conda-cheatsheet.pdf#toolbar=0&navpanes=0&scrollbar=0" type="application/pdf" width="100%" height="600px" /> -->

<object data="files/conda-cheatsheet.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="files/conda-cheatsheet.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="files/conda-cheatsheet.pdf">Download PDF</a>.</p>
    </embed>
</object>