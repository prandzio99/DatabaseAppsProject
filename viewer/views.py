from django.shortcuts import render, redirect
from .models import *
from .forms import *


# home
def home(request):
    return render(request, 'home.html')


# books
def book_list(request):
    content = {"books": Book.objects.all()}
    return render(request, 'bookList.html', content)


def book_form(request, book_id=0):
    if request.method == "GET":
        if book_id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(instance=book)
        return render(request, 'bookForm.html', {"form": form})
    else:
        if book_id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/books/list')


def book_delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('/books/list')


# addresses
def address_list(request):
    content = {"addresses": Address.objects.all()}
    return render(request, 'addressList.html', content)


def address_form(request, address_id=0):
    if request.method == "GET":
        if address_id == 0:
            form = AddressForm()
        else:
            address = Address.objects.get(pk=address_id)
            form = AddressForm(instance=address)
        return render(request, 'addressForm.html', {"form": form})
    else:
        if address_id == 0:
            form = AddressForm(request.POST)
        else:
            address = Address.objects.get(pk=address_id)
            form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
        return redirect('/address/list')


def address_delete(request, address_id):
    address = Address.objects.get(pk=address_id)
    address.delete()
    return redirect('/address/list')


# authors
def author_list(request):
    content = {"authors": Author.objects.all()}
    return render(request, 'authorList.html', content)


def author_form(request, author_id=0):
    if request.method == "GET":
        if author_id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=author_id)
            form = AuthorForm(instance=author)
        return render(request, 'authorForm.html', {"form": form})
    else:
        if author_id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=author_id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/authors/list')


def author_delete(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return redirect('/authors/list')


# publishers
def publisher_list(request):
    content = {"publishers": Publisher.objects.all()}
    return render(request, 'publisherList.html', content)


def publisher_form(request, publisher_id=0):
    if request.method == "GET":
        if publisher_id == 0:
            form = PublisherForm()
        else:
            publisher = Publisher.objects.get(pk=publisher_id)
            form = PublisherForm(instance=publisher)
        return render(request, 'publisherForm.html', {"form": form})
    else:
        if publisher_id == 0:
            form = PublisherForm(request.POST)
        else:
            publisher = Publisher.objects.get(pk=publisher_id)
            form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
        return redirect('/publishers/list')


def publisher_delete(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    publisher.delete()
    return redirect('/publishers/list')


# tags
def tag_list(request):
    content = {"tags": Tag.objects.all()}
    return render(request, 'tagList.html', content)


def tag_form(request, tag_id=0):
    if request.method == "GET":
        if tag_id == 0:
            form = TagForm()
        else:
            tag = Tag.objects.get(pk=tag_id)
            form = TagForm(instance=tag)
        return render(request, 'tagForm.html', {"form": form})
    else:
        if tag_id == 0:
            form = TagForm(request.POST)
        else:
            tag = Tag.objects.get(pk=tag_id)
            form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
        return redirect('/tags/list')


def tag_delete(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    tag.delete()
    return redirect('/tags/list')


# reading lists
def readinglist_list(request):
    content = {"readinglists": ReadingList.objects.all()}
    return render(request, 'readinglistList.html', content)


def readinglist_form(request, readinglist_id=0):
    if request.method == "GET":
        if readinglist_id == 0:
            form = ReadingListForm()
        else:
            readinglist = ReadingList.objects.get(pk=readinglist_id)
            form = ReadingListForm(instance=readinglist)
        return render(request, 'readinglistForm.html', {"form": form})
    else:
        if readinglist_id == 0:
            form = ReadingListForm(request.POST)
        else:
            readinglist = ReadingList.objects.get(pk=readinglist_id)
            form = ReadingListForm(request.POST, instance=readinglist)
        if form.is_valid():
            form.save()
        return redirect('/readinglists/list')


def readinglist_delete(request, readinglist_id):
    readinglist = ReadingList.objects.get(pk=readinglist_id)
    readinglist.delete()
    return redirect('/readinglists/list')


# book tags
def booktag_list(request):
    content = {"booktags": BookTag.objects.all()}
    return render(request, 'booktagList.html', content)


def booktag_form(request, booktag_id=0):
    if request.method == "GET":
        if booktag_id == 0:
            form = BookTagForm()
        else:
            booktag = BookTag.objects.get(pk=booktag_id)
            form = BookTagForm(instance=booktag)
        return render(request, 'booktagForm.html', {"form": form})
    else:
        if booktag_id == 0:
            form = BookTagForm(request.POST)
        else:
            booktag = BookTag.objects.get(pk=booktag_id)
            form = BookTagForm(request.POST, instance=booktag)
        if form.is_valid():
            form.save()
        return redirect('/booktags/list')


def booktag_delete(request, booktag_id):
    booktag = BookTag.objects.get(pk=booktag_id)
    booktag.delete()
    return redirect('/booktags/list')


# rlbs
def rlb_list(request):
    content = {"rlbs": ReadingListBook.objects.all()}
    return render(request, 'rlbList.html', content)


def rlb_form(request, rlb_id=0):
    if request.method == "GET":
        if rlb_id == 0:
            form = ReadingListBookForm()
        else:
            rlb = ReadingListBook.objects.get(pk=rlb_id)
            form = ReadingListBookForm(instance=rlb)
        return render(request, 'rlbForm.html', {"form": form})
    else:
        if rlb_id == 0:
            form = ReadingListBookForm(request.POST)
        else:
            rlb = ReadingListBook.objects.get(pk=rlb_id)
            form = ReadingListBookForm(request.POST, instance=rlb)
        if form.is_valid():
            form.save()
        return redirect('/readinglistbooks/list')


def rlb_delete(request, rlb_id):
    rlb = ReadingListBook.objects.get(pk=rlb_id)
    rlb.delete()
    return redirect('/readinglistbooks/list')
