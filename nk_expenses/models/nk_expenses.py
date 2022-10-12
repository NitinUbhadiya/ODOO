# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime


class Expenses(models.Model):
    _name = 'nk.expenses'
    _description = 'Expenses'
    _order = 'date desc'

    # =============== fields =============== #

    name = fields.Char()
    date = fields.Date(string = 'Date', required = True, default = datetime.today())
    expense_line = fields.One2many('nk.expense.line', 'expense_id', string = 'Expense Line')
    day_total = fields.Integer(compute = '_compute_day_total')
    transport_total = fields.Integer(compute = '_compute_day_total')

    # ========== Compute Methods =========== #

    @api.depends('expense_line')
    def _compute_day_total(recs):
        for self in recs:
            self.day_total = 0
            self.transport_total = 0
            for expense in self.expense_line:
                self.day_total += expense.spend
                if expense.expense_type_id.name == 'Transport':
                    self.transport_total += expense.spend
