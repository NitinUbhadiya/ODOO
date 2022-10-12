# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ExpenseLine(models.Model):
    _name = 'nk.expense.line'
    _description = 'Expense Line'

    # =============== fields =============== #

    name = fields.Char(string = 'Note')
    expense_type_id = fields.Many2one('nk.expense.type')
    spend = fields.Integer(string = 'Spend')
    # for nk.expenses's expense_line field(one2many)
    expense_id = fields.Many2one('nk.expenses')
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    sequence = fields.Char()
