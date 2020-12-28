# -*- coding: utf-8 -*-
{
    'name' : 'Cooperative Volunteers',
    'summary' : 'App for cooperative volunteers',
    'description' : 'Modulos for cooperative volunteers',
    'author' : 'Rosa Ortega',
    'category' : 'Training',
    'version' : '0.1',
    'depends' : ['base'],
    'data' : [
        'security/cooperative_volunteers_security.xml',
        'security/ir.model.access.csv',
        'views/cv_menuitems.xml',
        'views/cv_views.xml',
    ],
    'demo' : [
        'demo/cv_demo.xml'
    ],
}