# -*- coding: utf-8 -*-

from odoo import models, fields, api

    
class Books(models.Model):
    _name = 'library.books'
    _description = 'books of the library'
    
    name = fields.Char(string='Book',required=True)
    
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