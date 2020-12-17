# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
    
class Task(models.Model):
    _name = 'cooperative.volunteers.task'
    _description = 'Tasks may occurr more than one'
    
    name = fields.Char(string='Task name',required=True)
    description = fields.Text(string='Description')
    
    task_type = fields.Selection(string='Type',
                                selection=[('a','A'),
                                          ('b','B'),
                                          ('c','C')])
    start = fields.Datetime(string='Start')
    stop = fields.Datetime(string='Stop')
    
    repeats = fields.Boolean(string='Repeats')
    frequency = fields.Selection(string='Frequency',
                                selection=[('daily','Daily'),
                                          ('weekly','Weekly'),
                                          ('monthly','Monthly'),
                                          ('yearly','Yearly')])
    
    state = fields.Selection(string='State',
                                selection=[('draft','Draft'),
                                          ('ready','Ready'),
                                          ('in-progress','In-Progress'),
                                          ('done','Done'),
                                          ('cancel','Cancel')],
                            default='draft')
    leader = fields.Char(string='Leader')
    
    volunteer_ids = fields.Many2many(comodel_name='res.partner',string='Volunteers')
    
    @api.onchange('leader')
    def _onchange_leader(self):
        if self.leader and self.state == 'draft':
            self.state = 'ready'
        if not(self.leader):
            self.state = 'draft'
