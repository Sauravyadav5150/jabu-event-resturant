{
    'name': 'Version One Bus ',
    'version': '0.1',
    'category': 'Bus',
    'sequence': 15,
    'summary': 'this is bus ticket booking system',
    'installable': True, # this will show install button on apps 
    #  'data': [  "views/addCreateadby.xml"  ], #usuall some kind of master data  , views and so on 
     "data": [
        "security/ir.model.access.csv",
        "views/bus_view.xml",
        "views/menus.xml"
    ],
    'depends': ['base','base_setup']  #''' modules which will get installed before this  one '''
}

