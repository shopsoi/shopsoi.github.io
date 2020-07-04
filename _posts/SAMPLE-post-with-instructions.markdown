---
title: Sample post
subtitle: With instructions!
layout: default
tags: 
modal-id: 7
date: 2014-07-18
img: dreams.png
thumbnail: dreams-thumbnail.png
alt: image-alt
description: Lorem ipsum dolor sit amet, usu cu alterum nominavi lobortis. At duo novum diceret. Tantas apeirian vix et, usu sanctus postulant inciderint ut, populo diceret necessitatibus in vim. Cu eum dicam feugiat noluisse.
post_content: >
  Content. Lorem ipsum dolor sit amet, usu cu alterum nominavi lobortis. At duo novum diceret. Tantas apeirian vix et, usu sanctus postulant inciderint ut, populo diceret necessitatibus in vim. Cu eum dicam feugiat noluisse. Lorem ipsum dolor sit amet, usu cu alterum nominavi lobortis. At duo novum diceret. Tantas apeirian vix et, usu sanctus postulant inciderint ut, populo diceret necessitatibus in vim. Cu eum dicam feugiat noluisse. 
  Instructions on adding a new post
    1 the filename should be yyyy-mm-dd-anything.markdown
    2 for each new tag you add, go to the <root>/tag/ folder and copy one of the existing htmls; name the file as your tag. Update the "tag" field in the new file.
    3 if you want your tag to have multiple words in it, separate them with underscores ("_"). If you use whitespace instead of the underscore, Jekyll will treat words with spaces as separate tags.
    4 you need 2 versions of the same image, one for thumbnail (width 400, height anything (289), small file size), and a better one for the posts (600x450)
    5 images live under /img/blog/
    6 "description" is a short paragraph displayed on the post page between image and content, and on the tag page under the post title.
    7 Content should contain all the text you want to be shown only on the post page.
    8 Everything in post_content has to be indented (have at least 2 spaces in the beginning of the line)
    9 All images in the post should be lazy-loaded. For that, the class of img should have "lazyload" in it. E.g.
      <img class="img-circle img-responsive lazyload" ..> or <img class="lazyload" ..>
    10 To post the blogpost, open gitbash and 
      1. git status
      2. git add folder (e.g. _includes) and files
      3. git status to check if all was added
      4. git commit -m "name of changes"
      5. git push origin master
---
