{
    "name": "Password Policy",
    "summary": "Allow admin to set password security requirements.",
    "version": "1.0",
    "author": "Bac Ha Software",
    "category": "Base",
    "depends": ["auth_signup", "auth_password_policy_signup", 'hr', "auth_password_policy"],
    "website": "https://bachasoftware.com",
    "license": "LGPL-3",
    "data": [
        "data/cron_send_mail.xml",
        "views/password_expire_notification_templates.xml",
        "views/res_config_settings_views.xml",
        "views/res_users_views.xml",
        "views/signup_templates.xml",
        "security/ir.model.access.csv",
        "security/res_users_pass_history.xml",
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
