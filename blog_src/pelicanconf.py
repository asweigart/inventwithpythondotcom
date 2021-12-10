#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Al Sweigart'
SITENAME = 'The Invent with Python Blog'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = '%s.atom.xml'
FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_RSS = '%s.rss.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
        ('Twitter', 'https://twitter.com/AlSweigart',
         'fab fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'https://www.linkedin.com/in/al-sweigart-aa41703/',
         'fab fa-linkedin fa-fw fa-lg'),
        ('GitHub', 'https://github.com/asweigart',
         'fab fa-github-square fa-fw fa-lg'),
        )

STATIC_PATHS = ['blogstatic']
STATIC_CHECK_IF_MODIFIED = True
THEME = "voidy-bootstrap-inventwithpython"

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
FILENAME_METADATA = '(?P<slug>.*?)\.html'
OUTPUT_PATH = '../output/blog'



SITESUBTITLE ="Al Sweigart's writings on programming."
#SITETAG = "Text that's displayed in the title on the home page."

FONT_AWESOME_CDN_LINK = {
    'href': 'https://use.fontawesome.com/releases/v5.0.13/css/all.css',
    'integrity': 'sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp',
    'crossorigin': 'anonymous'
}

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
#CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
#SIDEBAR = "sidebar.html"

CUSTOM_ARTICLE_FOOTERS = ('./inventblogfooter.html', )
SKIP_COLOPHON = True