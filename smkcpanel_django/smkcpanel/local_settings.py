import os
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = 'smkcpanel.urls'

LOGIN_REDIRECT_URL = '/server'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'smkcpanel', 'templates'),
    #os.path.join(PROJECT_ROOT, 'smkcpanel', 'templates', 'allauth', 'plain', 'example'),
    os.path.join(PROJECT_ROOT, 'smkcpanel', 'dashboard', 'templates')
)

# TEMPLATE_DIRS += [os.path.join(PROJECT_ROOT, 'smkcpanel', 'templates')]
# TEMPLATE_DIRS += [os.path.join(PROJECT_ROOT, 'smkcpanel', 'dashboard', 'templates')]

# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_FILE_PATH = os.path.join(PROJECT_ROOT, '../var/sessions'),