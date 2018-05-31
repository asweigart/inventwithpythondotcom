#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Al Sweigart'
SITENAME = 'The Invent with Python Blog'
#SITEURL = 'http://localhost:8000/blog'
SITEURL = 'https://inventwithpython.com/blog'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/AlSweigart'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = ['blogstatic']
LOAD_CONTENT_CACHE = False

THEME = "voidy-bootstrap"

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
FILENAME_METADATA = '(?P<slug>.*?)\.html'

SKIP_COLOPHON = True


OUTPUT_PATH = '../static/blog'
#DISQUS_SITENAME = 'inventwithpython'
GOOGLE_ANALYTICS = 'UA-5459430-3'
