#Un comprador puede comprar a varios agricultores y un agricultor puede vender a varios compradores

from odoo import models, fields, api
            
            
class Comprador(models.Model):
    
    _name = "agricultores.comprador"
    
    
    nombre = fields.Char(string = "Nombre", required = True)
    telefono = fields.Integer(string = "Telefono", required = True)
    
    agricultores_clientes_ids = fields.Many2many("agricultores.agricultor", string = "Agricultores que son clientes")