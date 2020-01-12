#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jingmeng CUI'
SITENAME = 'Jingmeng CUI'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# THEME = 'blue-penguin'
THEME = 'pelican-blue'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
#SOCIAL = (('ocrid', 'https://orcid.org/0000-0003-3421-8457'),
#		  ('researchgate', 'https://www.researchgate.net/profile/Jingmeng_Cui'),
#		  ('linkedin', 'https://www.linkedin.com/in/cuijm'),
#         ('github', 'https://github.com/Sciurus365'),
#         ('twitter', 'https://twitter.com/CUI_Jingmeng'),
#         )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# all the following settings are *optional*

# HTML metadata
SITEDESCRIPTION = ''

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
)
# additional menu items
#MENUITEMS = (
#    ('GitHub', 'https://github.com/Sciurus365'),
# )

# pelican-blue settings
SIDEBAR_DIGEST = 'Research Master Student, Radboud University'

FAVICON = 'url-to-favicon'

# DISPLAY_PAGES_ON_MENU = True

# TWITTER_USERNAME = 'CUI_Jingmeng'

MENUITEMS = (('Home', 'https://sciurus365.github.io'),
			)
