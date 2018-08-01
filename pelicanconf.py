#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

#DOCUTILS_SETTINGS = {}
DELETE_OUTPUT_DIRECTORY = False
#OUTPUT_RETENTION = []

AUTHOR = 'Jordi Warmenhoven'
SITENAME = 'Penguinsula'
SITESUBTITLE = 'Python, Stats, Modelling & Stuff'
SITEURL = ''

THEME = '../pelican-themes/voidy-bootstrap'

#SITETAG = "Text that's displayed in the title on the home page."

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)
SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", "sb_taglist.html", )
SOCIAL = (('Twitter', 'https://twitter.com/penguinsula',
           'fa fa-twitter-square fa-fw fa-lg'),
          ('GitHub', 'https://github.com/jwarmenhoven',
           'fa fa-github-square fa-fw fa-lg'),
          ('LinkedIn', 'https://www.linkedin.com/in/jordi-warmenhoven-9650805/',
           'fa fa-linkedin-square fa-fw fa-lg'),
          )
# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

TWITTER_USERNAME = "penguinsula"

LOAD_CONTENT_CACHE = False

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'
LOCALE = 'en_US'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('PyMC3', 'http://pymc3.readthedocs.io/en/latest/'),)

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/penguinsula'),
#	  ('GitHub', 'https://github.com/jwarmenhoven'),
#	  ('LinkedIn', 'https://www.linkedin.com/in/jordi-warmenhoven-9650805/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

