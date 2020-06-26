from book_management.models import Book, PublishingCompany, Author, Category
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
        #list = ['Toán', 'Lí', 'Hóa', 'Văn', 'Sử', 'Địa', 'Lập Trình Web', 'Mạng máy tính','lí thuyết thống kê', ' Triết']
        authors = Author.objects.all()
        categorys = Category.objects.all()
        companys = PublishingCompany.objects.all()
        for i in range(0, records):
            Book.objects.create(
                name_book=faker.word() + ' book',
                author_id=random.choice(authors),
                category_id=random.choice(categorys),
                publishingCompany_id=random.choice(companys),
                publishingYear=faker.date_time(),

            )