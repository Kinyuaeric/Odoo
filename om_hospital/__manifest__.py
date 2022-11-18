
{
    'name': 'Hospital management system',
    'version': '12.0.1.0.0',
    'category': 'Extra tools',
    'summary': 'module for managing the hospital',
    'Author': 'eric',
    'description': 'Hospital management system in odoo framework',
    'depends': ['mail', 'base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'reports/report.xml',
        'reports/appointment.xml',
        'reports/patient_card.xml'
    ],
    'installable': True,
    'Application': True,
    'Auto_install': False,
    'license': 'LGPL-3',
}
