#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from todotodo.models import Friendship, FriendshipRequest, Persona, Category, PersonaPermission, Todo, TodoRequest
# from django_seed import Seed



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackerthon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         parser.add_argument(
#             '--number', default=2, type=int, help='this is test'
#         )
#     def handle(self, *args, **options):
#         number = options.get('number')
#         seeder = Seed.seeder()
#         seeder.add_entity(User, number, {
#             'is_staff': False,
#             'is_superuser': False,
#         })
#         seeder.execute()
#         self.stdout.write(self.style.SUCCESS(f'{number} users created'))