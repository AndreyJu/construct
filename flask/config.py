import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True

SECRET_KEY = "GfKy3ue_WaD_SoLo-d47d..42"

OPENID_PROVIDERS = [ 
    {'name': 'Google',
    'url': 'https://www.google.com/accounts/o8/id'},
    
    {'name': 'MyOpenID',
    'url': 'https://www.myopenid.com'}
 ]
