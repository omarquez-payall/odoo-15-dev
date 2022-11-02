# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import models, fields, api

class AccountAnalyticLine( models.Model):
    _inherit = 'account.analytic.line'

    line_type = fields.Many2one(
        string = "Tipo Registro",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    )


    def write(self, vals):

        result = super( AccountAnalyticLine, self).write(vals)

        if 'unit_amount' in vals and vals['unit_amount'] or 'name' in vals and vals['name'] or 'date' in vals and vals['date'] or 'employee_id' in vals and vals['employee_id'] and result:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado del empleado " + str(self.name) + " en fecha  " + str(self.date) + " las horas realizadas del registro de horas a " +  str(self.unit_amount),
                message_type = "comment"
            )
