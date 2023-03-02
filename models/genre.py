from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class Genre(models.Model):
    _name = 'imdb.genre'
    _description = 'Genre'

    name = fields.Char(required=True, translate=True)
    description = fields.Text()

    _sql_constraints = [
        ('unique_name', 'unique(name)', _('Genre must be unique'))
    ]
