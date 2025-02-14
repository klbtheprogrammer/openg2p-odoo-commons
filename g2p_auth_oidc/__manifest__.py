{
    "name": "OpenID Connect Authentication",
    "version": "17.0.1.0.0",
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "external_dependencies": {"python": ["python-jose"]},
    "depends": ["auth_oauth"],
    "data": [
        "views/auth_oauth_templates.xml",
        "views/auth_oauth_provider.xml",
        "views/res_users.xml",
    ],
}
