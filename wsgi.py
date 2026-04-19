import os
from django.core.wsgi import get_wsgi_application

# Ensure 'cancer_project' matches your folder name exactly (case-sensitive)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cancer_project.settings')

application = get_wsgi_application()