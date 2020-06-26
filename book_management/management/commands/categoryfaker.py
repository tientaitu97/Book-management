from book_management.models import Category
from faker import Faker
from django.core.management.base import BaseCommand

faker = Faker(['en-Us', ])


class Command(BaseCommand):
    help = 'Faker data'

    def add_arguments(self, parser):
        parser.add_argument('records', type=int, help='Create records')

    def handle(self, *args, **options):
        records = options['records']
        list_category = ['Chính trị – pháp luật', 'Khoa học công nghệ – Kinh tế', 'Văn hóa xã hội – Lịch sử',
                         'Văn học nghệ thuật', 'Giáo trình', 'Truyện, tiểu thuyết', 'Tâm lý, tâm linh, tôn giáo',
                         'Sách thiếu nhi']

        for i in range(0, records):
            Category.objects.create(
                name_category=list_category[i],

            )
