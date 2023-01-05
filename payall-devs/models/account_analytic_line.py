# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import models, fields, api
from datetime import datetime, timedelta, timezone
import math

class AccountAnalyticLine( models.Model):
    _inherit = 'account.analytic.line'

    line_type = fields.Many2one(
        string = "Tipo de Registro",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    )

    #def setLineType(self):
    #    for record in self:
    #        lineTypeSetted = self.env['project.task.create.timesheet'].search([('time_spent', '=', record.unit_amount), ('description', '=', record.name)])



    def convert_float_to_timestamp(self, unit_amount):

        seconds_per_day = 86400
        minutes_per_day = 1440

        minutos = unit_amount

        decimal, entero = math.modf(unit_amount)


        print(unit_amount)
        decimal_redondeado = (round(decimal,2) * 60)
        decimal_final = int((round(decimal_redondeado,0)))
        entero_final = int((round(entero,0)))
        # minutos_segundos = entero_final, ':', decimal_final, "h"
        minutos_segundos = f'{entero_final}:{decimal_final}h'
        print("El decimal es: " , int(decimal_final))
        print("El entero es: " , int(entero_final))

        return minutos_segundos


    def write(self, vals):

        mensajeDefault = ""
        userMessage = ""
        dateMessage = ""
        employeeMessage = ""
        taskTypeMessage = ""
        unitMessage = ""

        result = super( AccountAnalyticLine, self).write(vals)
        mensajeDefault = "Modificó al usuario <b>" + self.employee_id.name + "</b> el/los siguiente/s campo/s: <br/>";

        if 'name' in vals and vals['name'] and result:
            userMessage = mensajeDefault + "<b>Descripción</b> → " + self.name + "<br/>";
        if 'date' in vals and vals['date'] and result:
            dateMessage = mensajeDefault + "<b>Date</b> → " + str(self.date) + "<br/>"
        if 'employee_id' in vals and vals['employee_id'] and result:
            employeeMessage = mensajeDefault + "<b>Employee</b> → " + self.employee_id.name + "<br/>";
        if 'line_type' in vals and vals['line_type'] and result:
            taskTypeMessage = mensajeDefault + "<b>Tipo de Tarea</b> → " + str(self.line_type.name) + "<br/>";
        if 'unit_amount' in vals and vals['unit_amount'] and result:
            unitMessage = mensajeDefault + "<b>Horas</b> → " + str(self.convert_float_to_timestamp(self.unit_amount))

        self.sudo().task_id.message_post( body =
        userMessage + dateMessage +  employeeMessage + taskTypeMessage + str(unitMessage),
            message_type = "comment"
        )