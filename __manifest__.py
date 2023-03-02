# -*- coding: utf-8 -*-

{
    'name': 'imdb',
    'summary': 'Internet Movie Database',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/genre_data.xml',
        'views/genre_views.xml',
        'views/movie_views.xml',
        'views/menu.xml'
    ],
    'application': False
}
