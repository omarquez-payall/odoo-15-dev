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
        if 'date' in vals:
            old_date = vals['date']
        result = super( AccountAnalyticLine, self).write(vals)
        if 'name' in vals and vals['name'] and result:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado la descripcion del registro de horas a " + self.name + ". Y fecha: " + old_date,
                message_type = "comment"
            )
        if 'date' in vals and vals['date'] and result:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado la descripcion del registro de horas a " + str(self.date),
                message_type = "comment"
            )
        if 'time_spent' in vals and vals['unit_amount'] and result:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado las horas realizadas del registro de horas a " + self.unit_amount,
                message_type = "comment"
            )
        if 'employee_id' in vals and vals['employee_id'] and result:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado el empleado del registro de horas a " + self.employee_id,
                message_type = "comment"
            )
