# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employe_info(models.Model):
    _name = 'employe_info.employe_info'
    _description = 'employe_info.employe_info'
    def default_date(self):
        return fields.date.today()
    image_uploaded = fields.Image(string="Image", max_width=50, max_height=50)
    department = fields.Selection([
        ('Accounts and Finance', 'Accounts and Finance'),
        ('HR', 'HR'),
        ('Business development', 'Business development'),
        ('Infrastructures', 'Infrastructures'),
        ('Research and development', 'Research and development'),
        ('Learning and development', 'Learning and development'),
        ('IT services', 'IT services'),
        ('Product development', 'Product development'),
        ('Admin department', 'Admin department'),
        ('Security and transport', 'Security and transport'),
    ], string='Department', default='')
    position = fields.Char()
    full_name = fields.Char()
    blood = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ], string='Blood Group', default='')
    gender = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Intersex', 'Intersex'),
        ('Trans', 'Trans'),
        ('Personal', 'Personal'),
        ('Eunuch', 'Eunuch'),
    ], string='Gender', default='')
    surname_title = fields.Selection([
        ('S/O.', 'S/O'),
        ('D/O', 'D/O'),
    ], string='S/O or D/O ', default='')
    surname = fields.Char()
    salary = fields.Integer(string='Salary')
    joined = fields.Date(string='Joined From',default=lambda ln: ln.default_date())
    record = fields.Datetime(string='Record created on', readonly=True, default=fields.Datetime.now())
    phone = fields.Char(string='Phone number')
    Ephone = fields.Char(string='Emergrncy Phone number')
    cnic = fields.Char(string='CNIC number')
    ibn = fields.Char(string='Bank IBN number')
    pcc = fields.Integer(string='Police Character Certificate number')
    address = fields.Char()
    email = fields.Char()
