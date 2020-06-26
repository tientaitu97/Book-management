from book_management.models import LoanDetails, Book, LoanPayment
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
        list_book = Book.objects.all()
        list_payment = LoanPayment.objects.all()
        mylist = ["True", "False"]
        for i in range(0, records):
            LoanDetails.objects.create(
                loanPayment_id=random.choice(list_payment),
                book_id=random.choice(list_book),
                comment=faker.text(),
                have_paid=random.choice(mylist),
                pay_day=faker.date_time(),


            )