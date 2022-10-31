# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTask( models.Model):
    _inherit = 'project.task'

    sprint = fields.Integer(
        string = "Sprint",
        help = "Indique el número del sprint en el que está incluido el ítem"
    )

    priority_payall = fields.Many2one(
        string = "Prioridad",
        comodel_name = "payall.task.priority",
        help = "Clasifique el ítem de trabajo según su importancia"
    )

    peso = fields.Many2one(
        string = "Peso",
        comodel_name = "payall.task.peso",
        help = "Clasifique el ítem según la magnitud del trabajo requerido"
    )

    @api.onchange('peso')
    def task_notify_peso(self):
        self.sudo().message_post( body = 
            "El usuario " + self.env.user.display_name + " ha modificado el peso a  " + self.peso.name,
            message_type = "comment"
        )
