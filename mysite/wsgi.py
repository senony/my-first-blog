import os
import sys
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

path = '/home/seungho403/my-first-blog'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = StaticFilesHandler(get_wsgi_application())
