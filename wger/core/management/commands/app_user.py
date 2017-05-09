import json
import requests

from rest_framework.authtoken.models import Token
from django.core.urlresolvers import reverse
from django.core.management.base import BaseCommand, CommandError
from wger.core.models import UserProfile
from wger.core.models import User

from wger.core.models import ApiUser
from wger import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)

    def handle(self, **options):
        if User.objects.filter(username = options['username']) or User.objects.filter(email = options['email']):
            raise CommandError("{} already exists".format(options['username']))
        user = User.objects.create_user(username=options["username"],
                                        password=options["password"],
                                        email=options["email"])

        return 'Successfully saved app user'
