# -*- coding: utf-8 -*-
{
    "name" : "Expenses",
    "author" : "Nitin Ubhadiya",
    "website": "",
    "support": "",  
    "category": "Learning Odoo",
    "license": "OPL-1",
    "summary": "Manage your all daily expenses here.",
    "description": """Manage your all daily expenses here.""",  
    "version":"15.0.1",
    "depends" : ["base_setup","web"],
    "application" : True,
    "data" : [
        "security/ir.model.access.csv",
        "views/nk_expenses_views.xml",
        "views/nk_expense_type_views.xml",
        "views/nk_expenses_menues.xml",
    ],
    "auto_install":False,
    "installable" : True,
}
