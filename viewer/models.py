from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=8)
    local = models.CharField(max_length=8, blank=True, null=True)
    zip_code = models.CharField(max_length=8)
    city = models.CharField(max_length=255)

    def __str__(self):
        if self.local is None:
            if self.street is None:
                return str(self.city) + " " + str(self.building) + ", " + str(self.zip_code)
            else:
                return str(self.street) + " " + str(self.building) + ", " + str(self.zip_code) + " " + str(self.city)
        else:
            return str(self.street) + " " + str(self.building) + "/" + str(self.local) + ", " + str(self.zip_code)\
                   + " " + str(self.city)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    release_year = models.PositiveSmallIntegerField(default=1900)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.title) + ", " + str(self.author) + ", " + str(self.release_year)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class ReadingList(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)


class BookTag(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book) + ", tag: " + str(self.tag)


class ReadingListBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
    read = models.BooleanField()

    def __str__(self):
        return str(self.reading_list) + ", " + str(self.book)
