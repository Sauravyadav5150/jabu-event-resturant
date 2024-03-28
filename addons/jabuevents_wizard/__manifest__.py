{
    'name': 'Version One events ',
    'version': '0.1',
    'category': 'jabuevent',
    'sequence': 15,
    'summary': 'Only Data collection Wizard',
    'installable': True, # this will show install button on apps 
    "data": [
        "security/ir.model.access.csv",
        # "views/jabu_view.xml",
        # "views/menus.xml",
        # "views/sale_order.xml",
        "wizard/create_events.xml",
        "wizard/menues.xml",
        
        
    ],
    'depends': ['base','base_setup','sale_crm']  #''' modules which will get installed before this  one '''
}