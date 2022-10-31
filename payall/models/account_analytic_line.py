# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import models, fields, api

class AccountAnalyticLine( models.Model):
    _inherit = 'account.analytic.line'

    line_type = fields.Many2One(
        string = "Tipo Registro",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    )


    @api.onchange('name')
    def task_notify_name(self):
        if self.task_id:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado la descripcion del registro de horas a " + self.name,
                message_type = "comment"
            )
    
    @api.onchange('date')
    def task_notify_date(self):
        if self.task_id:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado la fecha del registro de horas a " + str(self.date),
                message_type = "comment"
            )
    
    @api.onchange('time_spent')
    def task_notify_hours(self):
        if self.task_id:
            self.sudo().task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado las horas realizadas del registro de horas a " + self.time_spent,
                message_type = "comment"
            )