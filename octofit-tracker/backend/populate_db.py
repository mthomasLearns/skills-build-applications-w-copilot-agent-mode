import os
import django
from django.conf import settings
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

def create_test_users():
    User.objects.create_user(username='testuser1', password='testpass1')
    User.objects.create_user(username='testuser2', password='testpass2')
    print('Test users created.')

if __name__ == "__main__":
    create_test_users()
