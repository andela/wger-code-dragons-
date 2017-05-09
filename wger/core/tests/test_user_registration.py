from django.contrib.auth.models import User
from wger.core.tests import api_base_test


class UserRegistrationTestCase(api_base_test.ApiPostTestCase):
    '''Tests registering a new user through the API'''
    object_class = User
    url = 'core:user:registration'
    data = {'username': 'felistas',
            'password1': 'shera',
            'password2': 'shera',
            'email': 'felistas.ngumi@andela.com'}


class ListUserTestCase(api_base_test.ApiGetTestCase):
    '''Tests listing users via the API'''
    object_class = User
    url = 'core:user:registration'
    data = {'username': 'felistas',
            'password1': 'shera',
            'password2': 'shera',
            'email': 'felistas.ngumi@andela.com'}
