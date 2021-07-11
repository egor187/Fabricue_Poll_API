from .settings import *


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # add browsable view - no need Postman to testing api on dev
    ]
}
