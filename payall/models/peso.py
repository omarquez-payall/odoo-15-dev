# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Peso(models.Model):
    _name = 'payall.task.peso'
    _description = 'Modelo para tener la referencia del peso de la tarea'

    name = fields.Char(
        string = "Peso"
    )

    # @api.constrains('name')
    # def _check_duplicates_peso(self):
    #     for record in self:
    #         record.value_peso = self.env['payall.task.peso'].search([('name', '=', record.peso.name)])
    #         if record.value_peso:
    #             raise ValidationError('El valor de peso ya está registrado')
    
    @api.onchnge('name')
    def _check_duplicates_peso(self):
        for record in self:
            record.name = self.env['payall.task.peso'].search([('name', '=', record.name)])
            if record.name:
                raise ValidationError('El valor de peso ya está registrado')
