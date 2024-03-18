{
    'name': 'Version One section ',
    'version': '0.1',
    'category': 'Section data',
    'sequence': 15,
    'summary': 'Learn and understand basics of odoo aned show me ',
    'installable': True, # this will show install button on apps 
    #  'data': [  "views/addCreateadby.xml"  ], #usuall some kind of master data  , views and so on 
     "data": [
        "security/ir.model.access.csv",
        "views/rest_view.xml",
        "views/menus.xml"
    ],
    'depends': ['base','base_setup']  #''' modules which will get installed before this  one '''
}

