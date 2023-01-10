{
    'name': 'Odoo Studio for Community',
    'version': '14.0.0.0',
    'category': 'Web',
    'summary': 'With this Odoo application, you can easily customize and build your own views without any technical expertise. It allows you to create new forms and fields, and make changes to existing forms, including editing the tree view and form view, as well as modifying pages, widgets, fields, and buttons. All of these modifications can be made on the fly.',
    'description': """
        This Odoo application allows you to:

    Customize and build your own views without any technical knowledge.
    Create new forms and fields.
    Make changes to existing forms, such as editing the tree view and form view.
    Modify pages, widgets, fields, and buttons.
    All of these modifications can be made on the fly.
    This application makes it easy for you to customize your views to meet your specific needs.
    It provides a user-friendly interface that allows you to make changes without any technical expertise.
    With this application, you have the flexibility to modify various aspects of your views, including the layout and content.
    You can easily add new elements or edit existing ones to create a view that meets your exact requirements.
    This application is a valuable tool for anyone looking to customize their Odoo views without needing technical skills.
    It allows you to make changes quickly and easily, helping you to get the most out of your Odoo system.
    Whether you are an experienced user or new to Odoo, this application is a useful resource for customizing your views to meet your specific needs.

    Odoo community studio
    Odoo studio
    Customization
    View creation
    Form creation
    Field creation
    Form editing
    Tree view editing
    Form view editing
    Page modification
    Widget modification
    Field modification
    Button modification
    User-friendly interface
    Non-technical customization
    On-the-fly modification
    Flexibility
    Layout modification
    Content modification
    Element addition
    Element editing
    View customization
    Requirements-specific views
    Technical expertise not required
    Quick changes
    Efficient customization
    Valuable tool
    Experienced user
    New user
    Resource for view customization
    Specific needs
    Odoo customization
    View customization tool
    Form customization
    Field customization
    Page customization
    Widget customization
    Button customization
    Easy customization
    Simple customization
    User-friendly customization
    """,
    'author': "medconsultantweb@gmail.com",
    'depends': ['web', "web_editor", "base_automation"],
    'data': [
        'views/templates.xml',
        'views/ir_ui_menu_view.xml',
        'views/report_kanban_view.xml',
        'security/view_dynamic_security.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/form_edit.xml',
        'static/src/xml/base.xml',
        'static/src/xml/form_fields.xml',
        'static/src/xml/kanban_template.xml',
        'static/src/xml/report_edit.xml',
    ],
    'images': ['images/main_screen.jpg'],
    'price': 200,
    'license': 'OPL-1',
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': [
        'static/description/module_image.jpg',
    ],
    'live_test_url': 'http://3.88.219.20:8071/web/login',

}
