import os
import django
from django.conf import settings
from django.core.management import call_command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
django.setup()
from faker import Faker
from catalog.models import Language, Author, Book, BookInstance
import random
import datetime 

fake = Faker()
Faker.seed(0)
def generate_languages(n):
    for i in range(n):
        lang = fake.language_name()
        language, created = Language.objects.get_or_create(lang=lang)
        if created:
            language.save()

def generate_authors(n):
    for i in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth(minimum_age=25, maximum_age=115)
        date_of_death = fake.date_between(start_date='-30y', end_date= 'today')
        author, created = Author.objects.get_or_create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, date_of_death=date_of_death)
        if created:
            author.save()

def generate_books(n):
    authors = Author.objects.all()
    languages = Language.objects.all()
    for i in range(n):
        title = fake.text()
        author = random.choice(authors)
        summary = fake.text()
        isbn = fake.isbn13()
        language = random.choice(languages)
        book = Book(title=title, author=author, summary=summary, isbn=isbn, language=language)
        book.save()

def generates_bookinstances(n):
    books = Book.objects.all()
    for i in range(n):
        id=fake.uuid4()
        book = random.choice(books)
        imprint = fake.text(max_nb_chars=50)
        due_back = fake.date_between(start_date='today', end_date='+30d')
        book_instance = BookInstance(id=id, book=book, imprint=imprint, due_back=due_back)
        book_instance.save()

generate_languages(5)
generate_authors(5)
generate_books(7)
generates_bookinstances(7)
