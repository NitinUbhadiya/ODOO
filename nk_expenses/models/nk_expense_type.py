# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ExpenseType(models.Model):
    _name = 'nk.expense.type'
    _description = 'Expense Type'

    # =============== fields =============== #

    name = fields.Char(string = 'Expense Type')
    # color = fields.Integer()
