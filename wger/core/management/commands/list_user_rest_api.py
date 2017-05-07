from django.core.management.base import BaseCommand, CommandError
from wger.core.models import ApiUser
from wger.core.models import User

class Command(BaseCommand):

    def handle(self, **options):
        all_users = ApiUser.objects.all()
        list_users = []
        for user in all_users:
            list_users.append([user.user.username, user.user.email])
