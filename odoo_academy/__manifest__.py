# -*- coding: utf-8 -*-
{
    'name' : 'Escuelita Odoo',
    'summary' : 'App de la escuelita de Odoo',
    'description' : 'Modulos para la app de la escuelita de Odoo',
    'author' : 'Rosa Ortega',
    'category' : 'Training',
    'version' : '0.1',
    'depends' : ['base'],
    'data' : [
        'security/academy_security.xml',
        'security/library_security.xml',
        'security/cooperative_volunteers_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    'demo' : [
        'demo/academy_demo.xml'
    ],
}