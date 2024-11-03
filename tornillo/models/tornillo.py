from odoo import models, fields

class Tornillo(models.Model):
    _name = 'almacen.tornillo'
    _description = 'Tornillo'

    nombre = fields.Char(string="Nombre", required=True)
    diametro = fields.Float(string="Diámetro (mm)", required=True)
    rosca = fields.Char(string="Tipo de Rosca", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True, default=0)