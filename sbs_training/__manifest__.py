# -*- coding: utf-8 -*-

{
    'name': 'Functional Training Odoo CE',
    'category': 'Extra Tools',
    'version': '14.0.1.0.0',
    'authr': 'Smart Business Solutions Ltd',
    'company': 'Smart Business Solutions Ltd',
    'website': 'https://www.smartbusiness.co.ug',
    
    'summary': 'Functional Training Odoo CE',
  
    'depends': ['website_slides'],
    'data': [
        'data/slide_channel_data.xml',
        'data/slide.slide.csv',
    ],
    'installable': True,
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}

