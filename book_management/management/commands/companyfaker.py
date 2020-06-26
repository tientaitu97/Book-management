from book_management.models import PublishingCompany
from faker import Faker
from django.core.management.base import BaseCommand

faker = Faker(['en-Us', ])


class Command(BaseCommand):
    help = 'Faker data'

    def add_arguments(self, parser):
        parser.add_argument('records', type=int, help='Create records')

    def handle(self, *args, **options):
        records = options['records']
        list = PublishingCompany.objects.all()

        for i in range(0, records):
            PublishingCompany.objects.create(
                name_company=faker.name(),
                address=faker.address(),
                email=faker.free_email(),

            )
