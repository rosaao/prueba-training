# -*- coding: utf-8 -*-

from odoo import models, fields, api
    
class Rental(models.Model):
    _name = 'library.rental'
    _description = 'rental history of the library'
    
    customer_id = fields.Many2one(comodel_name='res.partner',
                                  string='Customer',
                                  required=True)
    
    name = fields.Char(string='Name', related='customer_id.name')
    
    book_ids = fields.Many2many(comodel_name='library.book', string="Rented books")