from django.contrib import admin
from .models import Book, Card, Category, Author, LoanPayment, LoanDetails, Staff, Readers, PublishingCompany


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_book', 'author_id', 'category_id', 'publishingCompany_id', 'publishingYear')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_category']


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'comment')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_author', 'website', 'comment')


class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'card_id', 'staff_id', 'borrow_date']


class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = ['loanPayment_id', 'book_id', 'comment', 'have_paid', 'pay_day']


class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_staff', 'date', 'number']


class ReadersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_readers', 'address', 'card_id']


class PublishingCompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_company', 'address', 'email']


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(LoanPayment, LoanPaymentAdmin)
admin.site.register(LoanDetails, LoanDetailsAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Readers, ReadersAdmin)
admin.site.register(PublishingCompany, PublishingCompanyAdmin)
