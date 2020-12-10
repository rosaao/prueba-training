# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CooperativeVolunteers(models.Model):
    _name = 'cooperative.volunteers'
    _description = 'To split the work'
    
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
    