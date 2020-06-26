from book_management.models import Card
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

        cards = Card.objects.all()

        for i in range(0, records):
            Card.objects.create(
                start_date=faker.date(),
                end_date=faker.date(),
                comment=faker.text(),


            )