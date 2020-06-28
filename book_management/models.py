from django.db import models


# Create your models here.


class Author(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name_author = models.CharField(max_length=255, blank=False, null=False)
    website = models.CharField(max_length=255, blank=False, null=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_author

    class Meta:
        db_table = 'author'


class Category(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name_category = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return self.name_category

    class Meta:
        db_table = 'category'


class PublishingCompany(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name_company = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_company

    class Meta:
        db_table = 'publishing_company'


class Book(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name_book = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE, name='author')
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    publishingCompany_id = models.ForeignKey(PublishingCompany, blank=False, null=False, on_delete=models.CASCADE)
    publishingYear = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name_book

    class Meta:
        db_table = 'book'


class Card(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        db_table = 'card'


class Readers(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name_readers = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    card_id = models.ForeignKey(Card, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_readers

    class Meta:
        db_table = 'readers'


class Staff(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name_staff = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField()
    number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_staff

    class Meta:
        db_table = 'staff'


class LoanPayment(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    card_id = models.ForeignKey(Card, blank=False, null=False, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, blank=False, null=False, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()

    class Meta:
        db_table = 'loan_payment'


class LoanDetails(models.Model):
    loanPayment_id = models.ForeignKey(LoanPayment, blank=False, null=False, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE)
    comment = models.TextField()
    have_paid = models.BooleanField(null=True)
    pay_day = models.DateTimeField()

    class Meta:
        db_table = 'loan_details'
