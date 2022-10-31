# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAnalyticLine( models.Model):
    _inherit = 'account.analytic.line'


    @api.onchange('name')
    def task_notify_name(self):
        if self.task_id:
            self.task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado la descripcion del registro de horas a " + self.name +". En fecha " +
                str(fields.Datetime.now())
            )
    
    @api.onchange('date')
    def task_notify_date(self):
        if self.task_id:
            self.task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado la fecha del registro de horas a " + str(self.date) +". En fecha " +
                str(fields.Datetime.now())
            )
    
    @api.onchange('time_spent')
    def task_notify_hours(self):
        if self.task_id:
            self.task_id.message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado las horas realizadas del registro de horas a " + self.time_spent +". En fecha " +
                str(fields.Datetime.now())
            )