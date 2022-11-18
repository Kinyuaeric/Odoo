from odoo import api,models, fields,_
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit='sale.order'
    patient_name =  fields.Char(string='Patient Name')
    
    
class HospitalPatient(models.Model):
    _name='hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']  
    _description='patient records'
    _rec_name='patient_name'
    
    
    patient_name = fields.Char(string='Name',required=True,track_visibility='always')
    patient_age = fields.Integer('Age',track_visibility='always')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image') 
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                           index=True, default=lambda self:_('New'))

    
    gender = fields.Selection(
        string='gender',
        selection=[('male', 'male'), 
                   ('female', 'female')],
        default='male')
    
    age_group = fields.Selection(string='age group',compute='set_age_group', 
                                 selection=[('minor', 'minor'),
                                            ('major', 'major')],
                                 default='major')
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age < 18:
                rec.age_group ='minor'
            else:
                rec.age_group ='major'
        
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age<=5:
                raise ValidationError(_('The age must be greater than 5'))
            
    @api.model
    def create(self,vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                       'hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
