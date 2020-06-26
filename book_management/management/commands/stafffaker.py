from book_management.models import Staff
from faker import Faker
from django.core.management.base import BaseCommand
import random
faker = Faker(['en-Us', ])


class Command(BaseCommand):
    help = 'Faker data'

    def add_arguments(self, parser):
        parser.add_argument('records', type=int, help='Create records')

    def handle(self, *args, **options):
        records = options['records']

        for i in range(0, records):
            Staff.objects.create(
                name_staff=faker.name(),
                date=faker.date(),
                number=faker.phone_number(),

            )