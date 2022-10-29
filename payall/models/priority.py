# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Priority(models.Model):
    _name = 'payall.task.priority'
    _description = 'Modelo para tener la referencia del Sprint en la tarea'

    priority = fields.Char(
        string = "Prioridad"
    )
