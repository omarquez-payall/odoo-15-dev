# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTaskCreateTimesheet( models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    line_type = fields.Many2one(
        string = "Tipo Registro",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    )

    def save_timesheet(self):
        values = {
            'task_id': self.task_id.id,
            'project_id': self.task_id.project_id.id,
            'date': fields.Date.context_today(self),
            'name': self.description,
            'user_id': self.env.uid,
            'unit_amount': self.time_spent,
            'line_type': self.line_type.id
        }
        self.task_id.user_timer_id.unlink()
        return self.env['account.analytic.line'].create(values)