
from odoo import models, fields

LEVEL_SELECTION = [
    ('basic', 'Basic'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('expert', 'Expert'),
]

class ScsCompetency(models.Model):
    _name = 'scs.competency'
    _description = 'SCM Competency'
    _order = 'code'

    name = fields.Char(required=True)
    code = fields.Char(required=True, help='e.g., 1.1, 2.3')
    cluster_id = fields.Many2one('scs.cluster', required=True, ondelete='cascade')
    definition = fields.Text()
