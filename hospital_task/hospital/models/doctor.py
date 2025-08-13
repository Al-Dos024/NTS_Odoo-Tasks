from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone')