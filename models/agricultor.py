# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class Agricultor(models.Model):
    """
    Define un agricultor
    """
    #Nombre modelo y nombre modulo
    _name = "agricultores.agricultor"
    _description = "Define un agricultor"
    _rec_name = "apellidos"
    

    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string = "Apellidos", required = True)
    telefono = fields.Integer(string = "Numero de telefono", required = False)
    cantidad_cosecha = fields.Float(string = "Cantidad de cosecha",
                                    help = "Valor en toneladas", 
                                    compute = "_compute_cantidad_cosecha")  #Al ser un campo calculado no se
                                                                            #almacena por defecto en la BBDD
                                                                            #para guardarlo hay que usar store = True
                                                                            #el cual se puede usar para realizar busquedas
    cultivo_id = fields.Many2one("agricultores.cultivo", string = "Cultivo con el que trabaja ese agricultor" )
    #compradores_ids = fields.Many2many("agricultores.comprador", string = "Compradores")
    
    
    @api.depends("cultivo_id.superficie", "cultivo_id.categoria_cultivo")
    def _compute_cantidad_cosecha(self):
        """ for agricultor in self:
            if agricultor.cultivo_id.categoria_cultivo == "HOR":
                agricultor.cantidad_cosecha = agricultor.cultivo_id.superficie * 0.25
            elif agricultor.cultivo_id.categoria_cultivo == "FRU":
                agricultor.cantidad_cosecha = agricultor.cultivo_id.superficie * 0.5
            elif agricultor.cultivo_id.categoria_cultivo == "CER":
                agricultor.cantidad_cosecha = agricultor.cultivo_id.superficie * 1.5
            elif agricultor.cultivo_id.categoria_cultivo == "LEG":
                agricultor.cantidad_cosecha = agricultor.cultivo_id.superficie * 2
            elif agricultor.cultivo_id.categoria_cultivo == "OTR":
                agricultor.cantidad_cosecha = agricultor.cultivo_id.superficie * 1 """
                
        """ porcent = [("HOR", 0.25), ("FRU", 0.5), ("CER", 1.5), ("LEG", 2)]
        porcent[2] => ("CER", 1.5)
        for record in self:
            record.cantidad_cosecha = ""
            for tipo in porcent:
                if record.cultivo_id.categoria_cultivo == tipo[0]:
                    record.cantidad_cosecha = record.cultivo_id.superficie * tipo[1]
            if record.cantidad_cosecha == "":
                raise ValidationError("Tipo de cultivo introducido no existe") """
        
        porcent = {"HOR":0.25, "FRU":0.5, "CER":1.5, "LEG":2}
        _logger.info('hola mundo')
        for record in self:
            if record.cultivo_id == False or record.cultivo_id.categoria_cultivo == False:
                record.cantidad_cosecha = 0.0
                _logger.info(f'cantidad vale {record.cantidad_cosecha}')
            elif porcent.get(record.cultivo_id.categoria_cultivo) == None:
                _logger.info('hola mundo2')
                raise ValidationError("Tipo de cultivo introducido no existe")
            else:
                _logger.info('hola mundo3')
                record.cantidad_cosecha = porcent[record.cultivo_id.categoria_cultivo] * record.cultivo_id.superficie