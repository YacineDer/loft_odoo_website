# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class LoftWebsite(Website):

    @http.route()
    def index(self, **kw):
        return request.render('yd_website_loft.page_home', {
            'featured_projects': [],
        })