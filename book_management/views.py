from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import UserLoginForm, CreateUserForm, BookForm


# Create your views here.
def index(request):
    return render(request, 'book_management/index.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                messages.info(request, 'invalid credentials')
                return redirect('/')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'book_management/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/home')


def singup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'book_management/singup.html', context)


def proper_pagination(books, index):
    start_index = 0
    end_index = 7
    if books.number > index:
        start_index = books.number - index
        end_index = start_index + end_index
    return (start_index, end_index)


def search(request):
    match = Book.objects.all().order_by('-id')
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:

            match = Book.objects.filter(Q(name_book__icontains=srch) |
                                        Q(author__name_author__istartswith=srch) |
                                        Q(publishingCompany_id__name_company__istartswith=srch))
            if match:
                return render(request, 'book_management/search.html', {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    paginator = Paginator(match, 30)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(books, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]
    list_book = list(match)
    context = {'page_range': page_range, 'books': books, 'list_book': list_book}
    return render(request, 'book_management/search.html', context)


def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/search')
    context = {'form': form}
    return render(request, 'book_management/create_book.html', context)


def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/search')
    context = {'form': form}
    return render(request, 'book_management/create_book.html', context)


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('/search')
    context = {'item': book}
    return render(request, 'book_management/delete.html', context)
