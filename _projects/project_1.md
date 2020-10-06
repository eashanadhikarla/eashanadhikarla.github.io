---
title: "Astro-Turfing Review System"
collection: projects
permalink: /projects/project_1_cv
github: "https://github.com/eashanadhikarla/Astroturfing-Review-System"
doi:
time: 
cv: false
excerpt_separator: <!--more-->
---

{% capture my_include %}{% include_relative project_1_cv.md %}{% endcapture %}
{{ my_include | split: "---" | last | markdownify }}

<!--more-->