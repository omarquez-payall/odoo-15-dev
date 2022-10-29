# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Peso(models.Model):
    _name = 'payall.task.peso'
    _description = 'Modelo para tener la referencia del peso de la tarea'

    peso = fields.Char(
        string = "Peso"
    )