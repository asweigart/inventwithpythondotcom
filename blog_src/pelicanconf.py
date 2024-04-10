#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Al Sweigart'
SITENAME = 'The Invent with Python Blog'
SITEURL = 'http://localhost:8000/blog'
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 20

# Only generate feeds for publishconf.py version:
#FEED_ALL_ATOM = 'atom.xml'
#CATEGORY_FEED_ATOM = '{slug}.atom.xml'
#FEED_ALL_RSS = 'rss.xml'
#CATEGORY_FEED_RSS = '{slug}.rss.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
        #('Twitter', 'https://twitter.com/AlSweigart',
        # 'fab fa-twitter-square fa-fw fa-lg'),
        #('LinkedIn', 'https://www.linkedin.com/in/al-sweigart-aa41703/',
        # 'fab fa-linkedin fa-fw fa-lg'),
        #('GitHub', 'https://github.com/asweigart',
        # 'fab fa-github-square fa-fw fa-lg'),
        )


# NOTE: Changes to the theme's voidybootstrap.css file need to happen to
# C:\Users\Al\AppData\Local\Programs\Python\Python310\Lib\site-packages\pelican\themes\voidy-bootstrap-inventwithpython\static\css\voidybootstrap.css
# and pelican doesn't seem to have a way to change this? Not any way
# that actually works as far as I can tell.
THEME = "themes/voidy-bootstrap-inventwithpython"
#THEME_STATIC_DIR = '/blogstatic/theme'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
FILENAME_METADATA = r'(?P<slug>.*?)\.html'
OUTPUT_PATH = '../output/blog'
FAVICON = '../favicon.ico'


SITESUBTITLE ="Writings from the author of Automate the Boring Stuff."
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


# This is where I'm putting the ads for my other books:
CUSTOM_ARTICLE_FOOTERS = ('./inventblogfooter.html', )
SKIP_COLOPHON = True


#STATIC_PATHS = ['blogstatic']  # Don't use this, it causes the local pelican server to use locahost:8000 instead of localhost:8000/blog and makes it useless for testing.
STATIC_PATHS = []  # Get rid of " Watched path does not exist" warning for the images folder, which I don't use.
DELETE_OUTPUT_DIRECTORY = True


OPEN_GRAPH = True
OPEN_GRAPH_IMAGE = ''

TWITTER_USERNAME = "AlSweigart"


RELATIVE_URLS = False