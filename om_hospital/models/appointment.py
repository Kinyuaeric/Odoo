
from odoo import models,fields,api,_

class HospitalAppointment(models.Model):
        _name='hospital.appointment'
        _description='Appointment'
        _inherit=['mail.thread', 'mail.activity.mixin']

        
        
        @api.model
        def create(self,vals):
            if vals.get('name',_('New'))==_('new'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('new')
                result= super(HospitalAppointment,self).create(vals)
                return result  

        name= fields.Char(string='Appointment ID',required=True,copy=False,readonly=True,
                        index=True,default=lambda self:_('New'))
        patient_id = fields.Many2one(
            'hospital.patient',
            string='patient',
        required=True,
        )
        patient_age=fields.Integer('Age',related='patient_id.patient_age')
        
        notes=fields.Text(string='Registration Notes')
    
        doctor_note=fields.Text(string='Registration Note')
        pharmacy_note=fields.Text(string='Note')
        appointment_date=fields.Date(string='Date',required=True)
        state = fields.Selection([
            ('draft', 'Draft'), 
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
            
                                    
            ],string='status',readonly=True,default='draft')
        
        order_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                           index=True, default=lambda self:_('New'))
    