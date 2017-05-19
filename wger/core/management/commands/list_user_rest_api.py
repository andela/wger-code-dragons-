from django.core.management.base import BaseCommand, CommandError
from wger.core.models import ApiUser
from wger.core.models import User
from tabulate import tabulate


class Command(BaseCommand):

    def handle(self, **options):
        users = ApiUser.objects.all()
        all_users = []
        for user in users:
            all_users.append([user.user_id, user.user.username, user.user.email,
                              user.created_by_id])
        print(tabulate(all_users, headers=["USER ID", "USERNAME", "EMAIL",
                                           "CREATED BY ID"], tablefmt="fancy_grid"))
