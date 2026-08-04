from odoo import models, fields

class LoftProject(models.Model):
    _name = 'loft.project'
    _description = 'Loft Project'
    _order = 'sequence, id desc'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)
    image_ids = fields.One2many('loft.project.image', 'project_id', string='Images')
    short_description = fields.Text(translate=True)
    website_published = fields.Boolean(default=True)


class LoftProjectImage(models.Model):
    _name = 'loft.project.image'
    _description = 'Loft Project Image'
    _order = 'sequence, id'

    sequence = fields.Integer(default=10)
    name = fields.Char(translate=True)
    image = fields.Image(required=True)
    project_id = fields.Many2one('loft.project', required=True, ondelete='cascade')