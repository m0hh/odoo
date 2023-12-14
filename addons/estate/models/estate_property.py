from odoo import models,fields
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    name = fields.Char("Title",required=True)

    description = fields.Text("Description")

    postcode = fields.Char("Postcode")

    date_availability = fields.Date("Available From",copy=False,default=fields.Date.today()+relativedelta(months=3))

    expected_price = fields.Float(required=True)

    selling_price = fields.Float(readonly=True,copy=False)

    bedrooms = fields.Integer("Bedrooms",default=2)

    living_area = fields.Integer("Living Area (sqm)")

    facades = fields.Integer()

    garage = fields.Boolean()

    garden = fields.Boolean()

    garden_area = fields.Integer("Garden Area (sqm)")

    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'),("East","East"), ("West","West")],
        help="Type is used to separate Leads and Opportunities"
    )

    active = fields.Boolean("Active", default=True)

    state = fields.Selection(
        string='Type',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'),("offer_accepted","Offer Accepted"), ("sold","Sold"),("canceled","Canceled")],
        help="Type is used to separate Leads and Opportunities"
    )
