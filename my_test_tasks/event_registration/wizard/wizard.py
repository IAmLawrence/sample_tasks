from odoo import models, fields, api


class EventRegistrationWizard(models.TransientModel):
    _name = 'event.registration.wizard'

    @api.multi
    def generate_registrants(self):
        contacts_rec = self.env['event.registration.contacts'].search([])
        registrants_rec = self.env['event.registration.registrants'].search([])
        for each_rec in contacts_rec:
            for each_reg in registrants_rec:
                if each_reg.reg_email:
                    if each_reg.reg_email == each_rec.contacts_email:
                        print(each_reg.reg_name, ' Already in a Contact List.')
                        # each_reg.unlink()

                if each_reg.reg_contact:
                    if each_reg.reg_contact == each_rec.contacts_contact:
                        print(each_reg.reg_name, ' Already in a Contact List.')
                        # each_reg.unlink()

        lead_rec = self.env['event.registration.lead'].search([])
        contact_email_list = []
        contact_contact_list = []

        for each_lead in lead_rec:
            if each_lead.lead_email:
                contact_email_list.append(each_lead.lead_email)
            if each_lead.lead_contact:
                contact_contact_list.append(each_lead.lead_contact)
        print('contact_email_list>', contact_email_list)
        print('contact_contact_list>', contact_contact_list)

        for each_reg in registrants_rec:
            if each_reg.reg_email in contact_email_list:
                self.env['event.registration.contacts'].create({
                    'contacts_name': each_reg.reg_name,
                    'contacts_email': each_reg.reg_email,
                    'contacts_contact': each_reg.reg_contact,
                })

                self.env['event.registration.lead'].search([('lead_email', '=', each_reg.reg_email)]).unlink()

            elif each_reg.reg_contact in contact_contact_list:
                self.env['event.registration.contacts'].create({
                    'contacts_name': each_reg.reg_name,
                    'contacts_email': each_reg.reg_email,
                    'contacts_contact': each_reg.reg_contact,
                })
                self.env['event.registration.lead'].search([('lead_contact', '=', each_reg.reg_contact)]).unlink()
