from book_management.models import LoanPayment, Card, Staff
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
        list_card = Card.objects.all()
        list_staff = Staff.objects.all()
        for i in range(0, records):
            LoanPayment.objects.create(
                card_id=random.choice(list_card),
                staff_id=random.choice(list_staff),
                borrow_date=faker.date_time(),


            )