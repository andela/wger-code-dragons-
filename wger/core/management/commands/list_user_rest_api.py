from django.core.management.base import BaseCommand, CommandError
from wger.core.models import ApiUser
from wger.core.models import User


class Command(BaseCommand):

    def handle(self, **options):
        users = ApiUser.objects.all()
        all_users = []
        for user in users:
            all_users.append([user.user.username, user.user.email])
        print(all_users)
