# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):
    _name = 'spaceship'
    _description = 'To get to the moon'
    
    name = fields.Char(string='Spaceship', required=True)
    
    width = fields.Float(string='Width')
    length = fields.Float(string='Length')
    height = fields.Float(string='Height')
    
    fuel_type = fields.Selection(string='Fuel type',
                                selection=[('solid','Solid'),
                                          ('liquid','Liquid'),
                                          ('gas','Gas')])
    ship_type = fields.Char(string='Ship type')
    
    number_of_passengers = fields.Integer(string='Number of passengers')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.constrains('width','length')
    def _check_practical_design(self):
        for record in self:
            if record.width > record.length:
                raise UserError('This is not a practical design, make sure length is bigger than width.')