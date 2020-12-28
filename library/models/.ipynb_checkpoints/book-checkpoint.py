# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
    
class Book(models.Model):
    _name = 'library.book'
    _description = 'books of the library'
    
    name = fields.Char(string='Book',required=True)
    note = fields.Text(string='Note')
    
    authors = fields.Char(string='Authors')
    
    editors = fields.Char(string='Editors')
    
    publisher = fields.Char(string='Publisher')
    
    year_of_edition = fields.Integer(string='Year of edition')
    
    ISBN = fields.Char(string='ISBN')
    
    genre = fields.Selection(string='Genre',
                           selection=[('novel','Novel'),
                                     ('science','Science'),
                                     ('fiction','Fiction'),
                                     ('kids','Kids')])
    
    
    @api.onchange('ISBN')
    def _onchange_ISBN(self):
        if len(self.ISBN) != 13:
            raise ValidationError('ISBN must be 13 characters long.')