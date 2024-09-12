# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'NBS kursna lista',
    'version': '1.2',
    'category': 'Uncategorized',
    'summary': 'Narodna Banka Srbije kurs valuta',
    'author': 'Vladimir Pop',
    'description': """
        Narodna Banka Srbije kurs valuta, currency exchange 
    """,
    'depends': ['base'],
    'data': [

#        'GetCurrentExchangeRate/GetCurrentExchangeRate_soap1.1a.xml',
#        'GetCurrentExchangeRate/GetCurrentExchangeRate_soap1.1b.xml',
#        'GetCurrentExchangeRate/GetCurrentExchangeRate_soap1.2a.xml',
#        'GetCurrentExchangeRate/GetCurrentExchangeRate_soap1.2b.xml',
#        'GetCurrentExchangeRateByRateType/GetCurrentExchangeRateByRateType_soap1.1a.xml',
#        'GetCurrentExchangeRateByRateType/GetCurrentExchangeRateByRateType_soap1.1b.xml',
#        'GetCurrentExchangeRateByRateType/GetCurrentExchangeRateByRateType_soap1.2a.xml',
#        'GetCurrentExchangeRateByRateType/GetCurrentExchangeRateByRateType_soap1.2b.xml',
#        'GetCurrentExchangeRateList/GetCurrentExchangeRateList_soap1.1a.xml',
#        'GetCurrentExchangeRateList/GetCurrentExchangeRateList_soap1.1b.xml',
#        'GetCurrentExchangeRateList/GetCurrentExchangeRateList_soap1.2a.xml',
#        'GetCurrentExchangeRateList/GetCurrentExchangeRateList_soap1.2b.xml',
#        'GetExchangeRateListType/GetExchangeRateListType_soap1.1a.xml',
#        'GetExchangeRateListType/GetExchangeRateListType_soap1.1b.xml',
#        'GetExchangeRateListType/GetExchangeRateListType_soap1.2a.xml',
#        'GetExchangeRateListType/GetExchangeRateListType_soap1.2b.xml',
#        'GetServiceVersion/GetServiceVersion_soap1.1a.xml',
#        'GetServiceVersion/GetServiceVersion_soap1.1b.xml',
#        'GetServiceVersion/GetServiceVersion_soap1.2a.xml',
#       'GetServiceVersion/GetServiceVersion_soap1.2b.xml',
#        'lokacija_servera/lokacija.xml',
        'lokacija_servera/cron.xml',




    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {},
}
