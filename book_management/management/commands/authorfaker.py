from book_management.models import Author
from faker import Faker
from django.core.management.base import BaseCommand

faker = Faker(['en-Us', ])


class Command(BaseCommand):
    help = 'Faker data'

    def add_arguments(self, parser):
        parser.add_argument('records', type=int, help='Create records')

    def handle(self, *args, **options):
        records = options['records']
        authors = Author.objects.all()
        for _ in range(0, records):
            Author.objects.create(
                name_author=faker.name(),
                website=faker.dga(),
                comment=faker.paragraph(),

            )
