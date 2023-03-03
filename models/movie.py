# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

_CURRENT_YEAR = fields.Datetime.today().year


class Movie(models.Model):
    _name = 'imdb.movie'
    _description = 'Movie'

    @api.model
    def _default_year(self):
        return _CURRENT_YEAR

    @api.model
    def _last_10_years(self):
        return [(str(x), str(x)) for x in range(_CURRENT_YEAR + 1, _CURRENT_YEAR - 10, -1)]

    name = fields.Char(required=True)
    # year = fields.Selection(selection=lambda x: _last_10_years, string='Release year', default=_default_year)
    year = fields.Selection(selection='_last_10_years', string='Release year', default=_default_year)
    duration = fields.Integer(string='Duration (min)')
    duration_display = fields.Char(compute='_compute_duration_display', string='Duration')  # , store=True)
    description = fields.Text()
    genre_ids = fields.Many2many('imdb.genre', 'rel_movie_genre', string='Genres')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('check_duration', 'check(duration > 0)', _('Duration must be greater than 0'))
    ]

    @api.depends('duration')
    def _compute_duration_display(self):
        for movie in self:
            _ = movie.duration % 60
            movie.duration_display = '%dh %dmin' % (movie.duration // 60, _)

    def name_get(self):
        result = []
        for movie in self:
            name = '%s (%s)' % (movie.name, movie.year)
            result.append((movie.id, name))
        return result
