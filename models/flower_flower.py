from odoo import fields, models, api


class FlowerFlower(models.Model):
    _name = 'flower.flower'
    _description = 'Flower'

    name = fields.Char()
    scientific_name = fields.Char(required=True, translate=True, copy=False)
    date_from = fields.Date()
    date_to = fields.Date()
    watering_frequency = fields.Integer(required=True, help="Should be watered once every x days")
    watering_amount = fields.Float(required=True, help="In milliliters")

    def name_get(self):
        return [(record.id, '%s (%s)' % (record.name, record.scientific_name)) for record in self]