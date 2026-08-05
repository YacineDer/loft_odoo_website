# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class LoftWebsite(Website):

    def _loft_company_context(self):
        """Shared, sudo'd company/contact context used across all Loft pages."""
        website = request.website.sudo()
        company = website.company_id.sudo()
        partner = company.partner_id.sudo()

        company_address = ", ".join([
            x for x in [
                partner.street,
                partner.street2,
                partner.city,
                partner.zip,
                partner.country_id.name if partner.country_id else None,
            ] if x
        ])

        return {
            'company_phone': company.phone or '',
            'company_email': company.email or '',
            'company_address': company_address,
        }

    def _loft_published_projects(self, limit=None):
        domain = [('website_published', '=', True)]
        return request.env['loft.project'].sudo().search(
            domain, order='sequence, id desc', limit=limit
        )

    @http.route()
    def index(self, **kw):
        projects = self._loft_published_projects(limit=3)
        values = {'projects': projects}
        values.update(self._loft_company_context())
        return request.render('yd_website_loft.page_home', values)

    @http.route('/contactus', type='http', auth='public', website=True)
    def loft_contact_page(self, **kwargs):
        values = self._loft_company_context()
        return request.render('yd_website_loft.page_contact', values)

    @http.route('/contact/submit', type='http', auth='public', website=True, methods=['POST'])
    def loft_contact_submit(self, **post):
        # process form here
        return request.redirect('/contact?success=1')

    @http.route('/our-works', type='http', auth='public', website=True, sitemap=True)
    def our_works_page(self, **kwargs):
        projects = self._loft_published_projects()
        values = {'projects': projects}
        values.update(self._loft_company_context())
        return request.render('yd_website_loft.page_our_works_view', values)

    @http.route('/about-us', type='http', auth='public', website=True, sitemap=True)
    def about_us_page(self, **kwargs):
        projects = self._loft_published_projects()
        values = {'projects': projects}
        values.update(self._loft_company_context())
        return request.render('yd_website_loft.page_about_us_view', values)