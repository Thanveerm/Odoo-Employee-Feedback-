{
    'name': 'Employee Feedback',
    'version': '15.0.1.1.0',
    'sequence': 20,
    'description': """
        This module helps to send the employee feedback.
        """,

    'author': "Exbit softeare solutions",
    'company': 'Exbit sofware solutions',
    'maintainer': 'Exbit software solution',
    'website': "",
    'depends': ['hr','mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/employee_feddback.xml',
        'wizard/email_feedback.xml'
    ],
    'images':['static/description/banner.gif'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
