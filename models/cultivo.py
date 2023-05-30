# -*- coding: utf-8 -*-

from odoo import models, fields, api
            
            
class Cultivo(models.Model):
    """
    Define un cultivo
    """ 
    _name = "agricultores.cultivo"
    _description = "Define un cultivo"
    #Definicion del campo que se utilizara como dato a mostrar en las vistas de relaciones.
    #Si no se pone nada cogeria el de un campo llamado name (ojo!! no confundir con _name)
    _rec_name = "nombre"
    
    
    nombre = fields.Char(string = "Nombre", required = True)
    categoria_cultivo = fields.Selection([
        ("HOR", "Hortalizas"),
        ("FRU", "Frutas"), 
        ("CER", "Cereales"),
        ("LEG", "Legumbres"),
        ("OTR", "Otros")], 
        required = True, 
        string = "Categoria de cultivo")
    descripcion = fields.Text(string = "Descripcion", required = False)
    superficie = fields.Float(string = "Superficie hectareas", help = "Valor en hectareas", required = True)
    tipo_suelo = fields.Selection([
        ("FARC", "Franco arcilloso"), 
        ("FARE", "Franco arenoso"), 
        ("ARCI", "Arcilloso")], 
        string = "Tipo de suelo")
    fecha_siembra = fields.Date(string = "Fecha de siembra", required = True)
    fecha_cosecha = fields.Date(string = "Fecha de cosecha", required = True)
    agricultores_ids = fields.One2many("agricultores.agricultor", "cultivo_id", string = "Agricultores que trabajan en el campo") 