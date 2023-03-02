from random import randint

from odoo import api, models, fields, _


class Genre(models.Model):
    _name = 'imdb.genre'
    _description = 'Genre'

    @api.model
    def _default_color(self):
        return randint(1, 11)

    name = fields.Char(required=True, translate=True)
    description = fields.Text()
    color = fields.Integer(default=_default_color)

    _sql_constraints = [
        ('unique_name', 'unique(name)', _('Genre must be unique'))
    ]
