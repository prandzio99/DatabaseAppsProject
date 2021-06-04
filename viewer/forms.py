from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            "title": "Title",
            "publisher": "Publisher",
            "author": "Author",
            "release_year": "Release Year",
            "rating": "Rating (out of 5)",
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields["publisher"].empty_label = "Select"
        self.fields["author"].empty_label = "Select"
        self.fields["publisher"].required = False


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            "street": "Street",
            "building": "Building",
            "local": "Locale",
            "zip_code": "Zip Code",
            "city": "City",
        }

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields["street"].required = False
        self.fields["local"].required = False


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        labels = {
            "name": "Name",
            "url": "URL",
            "address": "Address",
        }

    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        self.fields["address"].empty_label = "Select"


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            "first_name": "Given Name(s)",
            "last_name": "Last Name",
            "url": "URL",
            "address": "Address",
        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields["address"].empty_label = "Select"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {
            "name": "Tag Name",
        }

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)


class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = '__all__'
        labels = {
            "title": "List Title",
        }

    def __init__(self, *args, **kwargs):
        super(ReadingListForm, self).__init__(*args, **kwargs)


class BookTagForm(forms.ModelForm):
    class Meta:
        model = BookTag
        fields = '__all__'
        labels = {
            "book": "Book",
            "tag": "Tag"
        }

    def __init__(self, *args, **kwargs):
        super(BookTagForm, self).__init__(*args, **kwargs)
        self.fields["book"].empty_label = "Select"
        self.fields["tag"].empty_label = "Select"


class ReadingListBookForm(forms.ModelForm):
    class Meta:
        model = ReadingListBook
        fields = '__all__'
        labels = {
            "book": "Book",
            "reading_list": "List",
            "read": "Did you read it already?",
        }

    def __init__(self, *args, **kwargs):
        super(ReadingListBookForm, self).__init__(*args, **kwargs)
        self.fields["book"].empty_label = "Select"
        self.fields["reading_list"].empty_label = "Select"
