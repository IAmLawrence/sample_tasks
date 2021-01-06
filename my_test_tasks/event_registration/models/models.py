# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventRegistrationRegistrants(models.Model):
    _name = 'event.registration.registrants'
    _rec_name = 'reg_name'

    reg_name = fields.Char(string="Name")
    reg_email = fields.Char(string="Email")
    reg_contact = fields.Char(string="Contact", size=10)


class EventRegistrationLead(models.Model):
    _name = 'event.registration.lead'
    _rec_name = 'lead_name'

    lead_name = fields.Char(string="Name")
    lead_email = fields.Char(string="Email")
    lead_contact = fields.Char(string="Contact", size=10)


class EventRegistrationContacts(models.Model):
    _name = 'event.registration.contacts'
    _rec_name = 'contacts_name'

    contacts_name = fields.Char(string="Name")
    contacts_email = fields.Char(string="Email")
    contacts_contact = fields.Char(string="Contact", size=10)
