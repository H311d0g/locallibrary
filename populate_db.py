import os
import django
from django.conf import settings
from django.core.management import call_command

# Set the environment variable to point to your project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

# Initialize Django
django.setup()
from catalog.models import Language, Genre, Author, Book, BookInstance
from faker import Faker
import random


fake = Faker()
Faker.seed(random.randint(1, 100))

def generate_languages(n):
    for i in range(n):
        lang = fake.language_name() # generates a random language name
        language = Language(lang=lang)
        language.save()
    generate_languages(5)
def generate_genre(n):
    for i in range(n):
        gen = fake.text()#generates a random genre
        genre = Genre(genre = genre)
        genre.save()
    generate_genre(15)

def generate_authors(n):
    for i in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth()
        date_of_death = fake.date_of_death()
        author = Author(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, date_of_death=date_of_death)
        author.save()
    generate_authors(70)

def generate_books(n):
    authors = Author.objects.all()
    genres = Genre.objects.all()
    languages = Language.objects.all()
    for i in range(n):
        title = fake.text(max_nb_chars=50)# generate a random title
        author = random.choice(authors)# choose a random author from the database
        summary = fake.text()# generate a random summaery
        isbn = fake.isbn13()# generate a random ISBN code
        genre = random.choice(genres) # choose a random genre from the database
        language = random.choice(languages)# choose a random language
        book = Book(title=title, author=author, summary=summary, isbn=isbn, genre=genre, language=language)
        book.save()
    generate_books(120)

def generate_bookinstance(n):
    books = Book.objects.all()
    for i in range(n):
        id = fake.uuid4() #generate a random UUID for the book instance
        book = random.choice(books) # choose a random book from the database
        imprint = fake.text(max_nb_chars=50) # generate a random imprint
        due_back = fake.date_between(start_date='today', end_date='+30d') # generate a random back date
        book_instance = BookInstance(id=id, book=book, imprint=imprint, due_back=due_back)
        book_instance.save()
    generate_bookinstance(120)