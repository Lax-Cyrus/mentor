{
    'name': 'Mentorship',
    'version': '1.0.1',
    'category': 'Education',
    'summary': 'Mentorship management',
    'description': """ 
        This moducle will provide functionality for managing mentees admission
        - Online admission form
        - Apllication tracking 
        -Document upload 
        - Status management
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/mentee_form_view.xml',
        'views/menuitems.xml',
        'views/mentee_admission_template.xml',
        'data/sequence.xml',
    ],
    'depends': ['base', 'mail', 'website'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}