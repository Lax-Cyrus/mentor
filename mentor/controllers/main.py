from odoo import http
from odoo.http import request

class AdmissionController(http.Controller):
    @http.route('/apply_now', type='http', auth='public', website=True)
    def admission_form(self, **kw):
        countries = request.env['res.country'].sudo().search([])
        return request.render('mentor.admission_form_template', {
            'countries': countries
        })

    @http.route('/admission/submit', type='http', auth='public', website=True, csrf=True)
    def submit_admission(self, **post):
        if post:
            vals = {
                'first_name': post.get('first_name'),
                'last_name': post.get('last_name'),
                'dob': post.get('dob'),
                'gender': post.get('gender'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'country': int(post.get('country')) if post.get('country') else False,
                'clas': post.get('clas'),
                # Parent details
                'pfname': post.get('pfname'),
                'plname': post.get('plname'),
                'nationality': int(post.get('nationality')) if post.get('nationality') else False,
                'tel': post.get('tel'),
                'mobile': post.get('mobile'),
                'city': post.get('city'),
                'occupation': post.get('occupation'),
                'pemail': post.get('pemail'),
                'district': post.get('district'),
                'subcounty': post.get('subcounty'),
                # Education background
                'current_school': post.get('current_school'),
                'time_in_sch': post.get('time_in_sch'),
                'state': 'submitted',
                #contact Person
                'contact_name':post.get('contact_name'),
                'contact_tel': post.get('contact_tel'),
                'contact_address': post.get('contact_address'),
                'contact_mobile': post.get('contact_mobile'),
                'relation': post.get('relation')
            }
            
            admission = request.env['admission'].sudo().create(vals)
            return request.render('mentor.admission_thanks', {
                'application': admission
            })
            
        return request.redirect('/apply_now')