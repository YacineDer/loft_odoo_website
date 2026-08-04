# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class LoftWebsite(Website):

    @http.route()
    def index(self, **kw):
        projects = request.env['loft.project'].sudo().search(
            [('website_published', '=', True)],
            order='sequence, id desc',
            limit=3,
        )
        return request.render('yd_website_loft.page_home', {
            'projects': projects,
        })

    @http.route('/contactus', type='http', auth='public', website=True)
    def loft_contact_page(self, **kwargs):
        return request.render('yd_website_loft.page_contact')

    @http.route('/contact/submit', type='http', auth='public', website=True, methods=['POST'])
    def loft_contact_submit(self, **post):
        # process form here
        return request.redirect('/contact?success=1')

    @http.route('/our-works', type='http', auth='public', website=True, sitemap=True)
    def our_works_page(self, **kwargs):
        projects = request.env['loft.project'].sudo().search(
            [('website_published', '=', True)],
            order='sequence, id desc'
        )
        return request.render('yd_website_loft.page_our_works_view', {
            'projects': projects,
        })

    @http.route('/about-us', type='http', auth='public', website=True, sitemap=True)
    def about_us_page(self, **kwargs):
        return request.render('yd_website_loft.page_about_us_view', {})