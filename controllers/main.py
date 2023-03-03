# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/imdb/v1/movies/list-all', methods=['GET'], auth='public', type='json')
    def list_all_movies(self, **kwargs):
        m = request.env['imdb.movie'].sudo()
        return m.search([('active', '=', True)])
