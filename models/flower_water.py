from odoo import fields, models, api

class FlowerFlowerWater(models.Model):
    _name = 'flower.water'
    _description = 'Flower water'

    lot_id = fields.Many2one('stock.lot')
    watering_datetime = fields.Datetime()


