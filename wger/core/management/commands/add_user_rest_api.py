import json
import requests


from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views, authenticate
from django.core.management.base import BaseCommand, CommandError
from wger.core.models import UserProfile
from wger.core.models import User

from wger.core.models import ApiUser
from wger import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('new_username', type=str)
        parser.add_argument('new_email', type=str)

    def handle(self, **options):
        user = User.objects.filter(username = options['username'])
        if user:
            response = requests.post(settings.SITE_URL+"/user/login",{"username": options['username'], "password": options['password']})
            print(response)
            if response.status_code == 200:
                token = json.loads(response.content)["key"]
                if User.objects.filter(username = options['new_username']) or User.objects.filter(email = options['new_email']):

                    raise CommandError("Username or email provided is already in use")
                else:
                    payload = {
                        "user":{
                            "username": options['new_username'],
                            "email": options['new_email'],
                            "password": '1234'
                        }
                    }
                    requests.post(settings.SITE_URL+'/api/v2/user/',
                                                headers={
                                                    'Authorization': 'Token '+token,
                                                    'content-type': 'application/json'
                                                },
                                                data=payload
                                                )
                    return 'Successfully saved user'



            else:
                return "Incorrect password"
        else:
            return "The username provided does not exist"
