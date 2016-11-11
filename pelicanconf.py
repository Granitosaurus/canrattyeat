#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Granitosaurus'
SITENAME = 'Can Ratty Eat'
SITESUBTITLE = 'What can and cannot your ratty eat?'
THEME = 'listheme'
SITEURL = ''
GITHUB_URL = 'http://github.com/granitosaurus/canrattyeat'
MENUITEMS = (
    ('Tags', '/tags.html'),
    ('General', '/pages/general.html'),
    ('FAQ', '/pages/faq.html'),
)
STATIC_PATHS = ['pages', 'extra/CNAME']
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
DISQUS_SITENAME = "canrattyeat"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
