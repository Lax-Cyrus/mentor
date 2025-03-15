from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Admission(models.Model):
    _name = "admission"
    _description = "Mentee admission"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    #mentee details 
    name = fields.Char(string='Name', required=False, translate=True)
    first_name = fields.Char(string ='First Name', required=True, tracking=True)
    last_name = fields.Char(string='Last Name', required=True, tracking=True)
    app_number = fields.Char(string='Application Number', readonly=True, copy=False, defualt= 'New')
    dob = fields.Date(string="Date of Birth", required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, tracking=True)
    email = fields.Char(string='Email', required=False, tracking=True)
    phone = fields.Char(string='Phone', required=False, tracking=True)
    country = fields.Many2one('res.country', string='Nationality')
    clas = fields.Selection([
            ('p1-p2', 'P1-P2'),
            ('p3-p4', 'P3-P4'),
            ('p5-p7', 'P5-P7'),
            ('s1-s4', 'S1-S4'),
            ('s5-s6', 'S5-S6'),
            ('s6_vacist', 'S6 Vacist'),
            ('s6_vacist', 'S6 Vacist'),
            ('other tertiary student', 'Other Tertiary Student'),
            ('non student', 'Non Student'),
        ],string='Class', tracking=True)

    #parent details
    pfname = fields.Char(string='First Name', required=True, tracking=True)
    plname = fields.Char(string='Last Name', tracking=True)
    nationality = fields.Many2one('res.country', string='Nationality', tracking=True)
    tel = fields.Char(string='Tel', tracking=True, required=True)
    mobile = fields.Char(string='Mobile', tracking=True)
    city = fields.Char(string='City', tracking=True)
    occupation = fields.Char(string='Occupation', tracking=True)
    pemail = fields.Char(string='Email', tracking=True)
    district = fields.Char(string='District', required=True, tracking=True)
    subcounty = fields.Char(string='Subcounty', tracking=True)
    
    
    
    #contact person
    contact_mobile = fields.Char(string='Mobile', tracking=True, required=True)
    contact_tel = fields.Char(string='Tel', tracking=True)
    contact_address = fields.Char(string= 'Contact Person Address')
    contact_name = fields.Char(string='Contact Person Name', tracking=True, required=True)
    relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'mother'),
        ('gaurdian', 'Guardian'),
        ('brother','Brother'),
        ('sister', 'Sister'),
    ], string='Relation with Contact Person', tracking=True, required=True)

    #Educatioon background
    current_school = fields.Char(string='Current School', tracking=True)
    # sch_location = 


    # previous_school = fields.Char(string='Previous School', tracking=True)
    time_in_sch = fields.Char(string='Time in current School', tracking=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], defualt='draft',string='Status', tracking=True)


    @api.model
    def create(self, vals):
        if vals.get('app_number', 'New') == 'New':
            vals['app_number'] = self.env['ir.sequence'].next_by_code('admission') or 'New'
        return super(Admission, self).create(vals)


    # def action_submit(self):
    #     self.state = 'submitted'

    # def action_review(self):
    #     self.state = 'review'

    # def action_approve(self):
    #     self.state = 'approved'

    # def action_reject(self):
    #     self.state ='rejected'

    @api.constrains('dob')
    def check_dob(self):
        for rec in self:
            if rec.dob:
                today = fields.Date.today()
                age = today.year - rec.dob.year - ((today.month, today.day) < (rec.dob.month, rec.dob.day))
                if age < 9:
                    raise ValidationError('Mentee must be at Least 9 years of age')
                if rec.dob > today:
                    raise ValidationError('Date of Birth can not be ahead of today')
    @api.onchange(first_name, last_name)
    def onchange_name(self):
        # for self in name
        self.name = str(self.first_name) + str(self.last_name)
    
    # partner_id =self.env['res.partner'].create({'name':self.name})