# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = 'spaceship'
    _description = 'To get to the moon'
    
    name = fields.Char(string='Spaceship', required=True)
    
    width = fields.Float(string='Width')
    height = fields.Float(string='Height')
    depth = fields.Float(string='Depth')
    
    fuel_type = fields.Selection(string='Fuel type',
                                selection=[('solid','Solid'),
                                          ('liquid','Liquid'),
                                          ('gas','Gas')])
    ship_type = fields.Char(string='Ship type')
    
    number_of_passengers = fields.Integer(string='Number of passengers')
    
    active = fields.Boolean(string='Active', default=True)
    