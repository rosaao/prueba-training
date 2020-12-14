# -*- coding: utf-8 -*-
{
    'name' : 'Library',
    'summary' : 'App for managing a library',
    'description' : 'Modulos for managing a library',
    'author' : 'Rosa Ortega',
    'category' : 'Training',
    'version' : '0.1',
    'depends' : ['base'],
    'data' : [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/library_views.xml',
    ],
    'demo' : [
        'demo/library_demo.xml'
    ],
}