REM This file only applies to Al's personal laptop.

REM Running `pelican` updates the .html blog files and puts them in ./output
REM But it doesn't copy static files from ./static/blogstatic to ./output
REM Run this batch file to do that, by running generateSite.py.

REM The template is in C:\Users\Al\AppData\Local\Programs\Python\Python310\Lib\site-packages\pelican\themes\voidy-bootstrap-inventwithpython

cd C:\github\inventwithpythondotcom\blog_src
C:\Users\Al\AppData\Local\Programs\Python\Python311\Scripts\pelican.exe -s publishconf.py
cd ..
py -3.11 generateSite.py
