from random import randint

from odoo import api, models, fields, _
from odoo.osv import expression


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

    @api.model
    def _name_search(self, name=None, args=None, operator='ilike', limit=100, name_get_uid=None):
        # [('name', '=', 'geronimo')]
        # [('name', '=', 'john'), ('description', '=', 'python')]  # AND
        # ['|', ('name', '=', 'john'), ('description', '=', 'python')]  # OR
        # ['|', '|', ('name', '=', 'john'), ('description', '=', 'python'), ('active', '=', True)]  # OR
        if not args:
            args = []
        if name:
            domain = [
                '|',
                ('name', operator, name),
                ('description', operator, name)
            ]
            domain = expression.AND([args, domain])
            _ids = list(self._search(domain, limit=limit, access_rights_uid=name_get_uid))
        else:
            _ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return _ids
