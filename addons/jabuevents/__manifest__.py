{
    'name': 'Version One events ',
    'version': '0.1',
    'category': 'jabuevent',
    'sequence': 15,
    'summary': 'this is event details of jabu',
    'installable': True, # this will show install button on apps 
    #  'data': [  "views/addCreateadby.xml"  ], #usuall some kind of master data  , views and so on 
     "data": [
        "security/ir.model.access.csv",
        "views/jabu_view.xml",
        "views/menus.xml"
        "views/sales_order.xml"
        
        
    ],
    'depends': ['base','base_setup','crm']  #''' modules which will get installed before this  one '''
}

