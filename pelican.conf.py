#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"QBank"
SITEURL = 'http://markbetnel.com/qbank'

TIMEZONE = 'America/New_York'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

# Blogroll
LINKS =  (
    ('SAGE', 'http://sagemath.org/'),
    ('Wolfram Alpha', 'http://www.wolframalpha.com/'),
    ('Khan Academy', 'http://www.khanacademy.org'),
    ('Math Fun Facts', 'http://www.math.hmc.edu/funfacts/'),
    ('R - Statistics', 'http://cran.r-project.org'),
    ('DESMOS', 'http://www.desmos.com')	
        )

# Social widget
SOCIAL = (
         ('HomeworkFeed', SITEURL + '/feeds/homework.atom.xml'),
         ('LessonsFeed', SITEURL + '/feeds/lessons.atom.xml'),
	 ('QuizzesFeed', SITEURL + '/feeds/quizzes.atom.xml')
	 )

DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    
