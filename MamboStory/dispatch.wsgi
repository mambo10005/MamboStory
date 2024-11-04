import os, sys

# edit your path below
sys.path.append("/home/manhojoung.helioho.st/httpdocs/MamboStory")

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MamboStory.settings')
application = get_wsgi_application()