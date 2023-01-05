{
    'name': 'Odoo Studio for Community',
    'version': '15.0.0.0',
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
        # 'views/templates.xml',
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
    'assets': {
        'web.assets_qweb': [
            '/studio_for_community/static/src/js/navbar/nabar_view.xml',
            '/studio_for_community/static/src/xml/base.xml',
            '/studio_for_community/static/src/xml/form_edit.xml',
            '/studio_for_community/static/src/xml/form_fields.xml',
            '/studio_for_community/static/src/xml/kanban_template.xml',
            '/studio_for_community/static/src/xml/report_edit.xml',
        ],
        'web.assets_backend': [
            'studio_for_community/static/src/css/daterangepicker.css',
            'studio_for_community/static/src/scss/menu_edit.scss',
            'studio_for_community/static/src/scss/edit_view_controller.scss',
            'studio_for_community/static/src/scss/basic_field.scss',
            'studio_for_community/static/src/scss/list_edit.scss',
            'studio_for_community/static/src/scss/form_edit.scss',
            'studio_for_community/static/src/scss/calendar_edit.scss',
            'studio_for_community/static/src/scss/pivot_edit.scss',
            'studio_for_community/static/src/scss/kanban_edit.scss',
            'studio_for_community/static/src/scss/graph_edit.scss',
            'studio_for_community/static/src/scss/search.scss',
            'studio_for_community/static/src/scss/report.scss',
            'studio_for_community/static/src/js/libs/jquery.js',
            'studio_for_community/static/src/libs/daterangepicker.js',
            'studio_for_community/static/src/libs/jquery.stickytableheaders.js',
            'studio_for_community/static/src/js/views/list/list_renderer.js',
            'studio_for_community/static/src/js/views/search/search_view.js',
            'studio_for_community/static/src/js/views/form/form_view.js',
            'studio_for_community/static/src/js/views/form/form_controller.js',
            'studio_for_community/static/src/js/chrome/menu.js',
            'studio_for_community/static/src/js/widgets/data_export.js',
            'studio_for_community/static/src/js/widgets/model_field_selector.js',
            'studio_for_community/static/src/js/views/edit_views/automation_access/automations.js',
            'studio_for_community/static/src/js/views/edit_views/basic_fields.js',
            'studio_for_community/static/src/js/views/edit_views/edit_view.js',
            'studio_for_community/static/src/js/views/edit_views/list/list_edit.js',
            'studio_for_community/static/src/js/views/edit_views/list/list_content.js',
            'studio_for_community/static/src/js/views/edit_views/list/list_property.js',
            'studio_for_community/static/src/js/views/edit_views/form/form_edit.js',
            'studio_for_community/static/src/js/views/edit_views/form/form_content.js',
            'studio_for_community/static/src/js/views/edit_views/form/form_property.js',
            'studio_for_community/static/src/js/views/edit_views/calendar/calendar_edit.js',
            'studio_for_community/static/src/js/views/edit_views/calendar/calendar_content.js',
            'studio_for_community/static/src/js/views/edit_views/calendar/calendar_property.js',
            'studio_for_community/static/src/js/views/edit_views/pivot/pivot_edit.js',
            'studio_for_community/static/src/js/views/edit_views/pivot/pivot_content.js',
            'studio_for_community/static/src/js/views/edit_views/pivot/pivot_property.js',
            'studio_for_community/static/src/js/views/edit_views/graph/graph_edit.js',
            'studio_for_community/static/src/js/views/edit_views/graph/graph_content.js',
            'studio_for_community/static/src/js/views/edit_views/graph/graph_property.js',
            'studio_for_community/static/src/js/views/edit_views/kanban/kanban_edit.js',
            'studio_for_community/static/src/js/views/edit_views/kanban/kanban_content.js',
            'studio_for_community/static/src/js/views/edit_views/kanban/kanban_property.js',
            'studio_for_community/static/src/js/views/edit_views/report/ReportKanBan.js',
            'studio_for_community/static/src/js/views/edit_views/report/ReportContent.js',
            'studio_for_community/static/src/js/views/edit_views/report/ReportEdit.js',
            'studio_for_community/static/src/js/views/edit_views/report/ReportProperty.js',
            'studio_for_community/static/src/js/views/abstract_controller.js',
            'studio_for_community/static/src/js/views/base.js',
            'studio_for_community/static/src/js/views/edit_views/start.js',
            'studio_for_community/static/src/js/views/edit_views/studioEditor.js',
            'studio_for_community/static/src/js/views/edit_views/viewContainer.js',
            'studio_for_community/static/src/js/navbar/navbar.js',
        ],
    },
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
}
