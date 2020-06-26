from book_management.models import Readers, Card
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
        list = Card.objects.all()

        for i in range(0, records):
            Readers.objects.create(
                name_readers=faker.name(),
                address=faker.address(),
                card_id=list[i],

            )