# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class Movie(models.Model):
    _name = 'imdb.movie'
    _description = 'Movie'

    name = fields.Char(required=True, translate=True, help='The description')

    _sql_constraints = [
        ('unique_name', 'unique(name)', _('Movie must be unique'))
    ]
