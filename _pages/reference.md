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

Build Docker: $\;\;\;\;\;\;\;\;\;\;\;\;$ `docker build -t <container-name> .`<br />
Run Docker: $\;\;\;\;\;\;\;\;\;\;\;\;\;$ `docker run -it -rm --name test --privileged <container-name>:<tag> bash`

Python Virtual Environment
======
On maxOS and Linux:

`python3 -m venv <path-to-env/env-name>`<br />
`source env/bin/activate # To activate the environment`<br />
`deactivate # To deactivate the environment`

Conda
======
## Getting Started

Verify Conda is installed, check version number: $\;\;\;\;\;\;\;\;\;\;\;\;$ `conda info`<br />
Update Conda to the current version: $\;\;\;\;\;\;\;\;\;\;\;\;$ `conda update -n base conda`<br />
Update all packages to the latest version of Anaconda.<br /> Will install stable and compatible versions,<br /> not necessarily the very latest: $\;\;\;\;\;\;\;\;\;\;\;\;$ `conda update anaconda`<br />

## Working with Environments

Create a new environment named ENVNAME with specific version of Python and packages installed: `conda create --name ENVNAME python=3.6
"PKG1>7.6" PKG2`<br />
