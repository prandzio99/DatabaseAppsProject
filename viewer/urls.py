from django.urls import path
from .views import *

urlpatterns = [

    # home
    path('', home, name="home"),

    # books
    path('books/list', book_list, name="book_list"),
    path('books/add', book_form, name="add_book"),
    path('books/<int:book_id>', book_form, name="edit_book"),
    path('books/delete/<int:book_id>', book_delete, name="delete_book"),

    # addresses
    path('address/list', address_list, name="address_list"),
    path('address/add', address_form, name="add_address"),
    path('address/<int:address_id>', address_form, name="edit_address"),
    path('address/delete/<int:address_id>', address_delete, name="delete_address"),

    # authors
    path('authors/list', author_list, name="author_list"),
    path('authors/add', author_form, name="add_author"),
    path('authors/<int:author_id>', author_form, name="edit_author"),
    path('authors/delete/<int:author_id>', author_delete, name="delete_author"),

    # publishers
    path('publishers/list', publisher_list, name="publisher_list"),
    path('publishers/add', publisher_form, name="add_publisher"),
    path('publishers/<int:publisher_id>', publisher_form, name="edit_publisher"),
    path('publishers/delete/<int:publisher_id>', publisher_delete, name="delete_publisher"),

    # tags
    path('tags/list', tag_list, name="tag_list"),
    path('tags/add', tag_form, name="add_tag"),
    path('tags/<int:tag_id>', tag_form, name="edit_tag"),
    path('tags/delete/<int:tag_id>', tag_delete, name="delete_tag"),

    # reading lists
    path('readinglists/list', readinglist_list, name="readinglist_list"),
    path('readinglists/add', readinglist_form, name="add_readinglist"),
    path('readinglists/<int:readinglist_id>', readinglist_form, name="edit_readinglist"),
    path('readinglists/delete/<int:readinglist_id>', readinglist_delete, name="delete_readinglist"),

    # books-tags
    path('booktags/list', booktag_list, name="booktag_list"),
    path('booktags/add', booktag_form, name="add_booktag"),
    path('booktags/<int:booktag_id>', booktag_form, name="edit_booktag"),
    path('booktags/delete/<int:booktag_id>', booktag_delete, name="delete_booktag"),

    # reading lists-books
    path('readinglistbooks/list', rlb_list, name="rlb_list"),
    path('readinglistbooks/add', rlb_form, name="add_rlb"),
    path('readinglistbooks/<int:rlb_id>', rlb_form, name="edit_rlb"),
    path('readinglistbooks/delete/<int:rlb_id>', rlb_delete, name="delete_rlb"),

]
