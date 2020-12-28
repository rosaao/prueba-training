# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'space.mission'
    _description = 'for multiple spaceship missions'
    
    spaceship_id = fields.Many2one(comodel_name='spaceship',string='Assigned Spaceship')
    name = fields.Char(string='Mission')
    
    crew_member_ids = fields.Many2many(comodel_name='res.partner',string='Crew members')
    
    launch_date = fields.Date(string='Launch date')
    return_date = fields.Date(string='Return date')
    