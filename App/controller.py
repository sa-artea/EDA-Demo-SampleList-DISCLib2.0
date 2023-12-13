
import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    # control['model'] = model.newCatalog()
    control['model'] = model.new_catalog()
    return control


# Funciones para la carga de datos


def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    books, authors = loadBooks(catalog)
    tags = loadTags(catalog)
    booktags = loadBooksTags(catalog)
    # sortBooks(catalog)
    return books, authors, tags, booktags


def loadBooks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = cf.data_dir + 'GoodReads/books.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        # model.addBook(catalog, book)
        # print(book, type(book))
        # book = format_book(book)
        model.add_book(catalog, book)
    # return model.bookSize(catalog), model.authorSize(catalog)
    return model.books_size(catalog), model.authors_size(catalog)


def format_book(book):
    int_key_lt = [
        "book_id",
        "goodreads_book_id",
        "best_book_id",
        "work_id",
        "books_count",
        "ratings_count",
        "work_ratings_count",
        "work_text_reviews_count",
        "ratings_1",
        "ratings_2",
        "ratings_3",
        "ratings_4",
        "ratings_5",
    ]

    big_int_key_lt = [
        "isbn13",
    ]

    float_key_lt = [
        "average_rating",
    ]

    str_key_lt = [
        "authors",
        "original_title",
        "title",
        "isbn",
        "isbn13",
        "original_publication_year",
        "language_code",
        "image_url",
        "small_image_url",
    ]

    for key in int_key_lt:
        book[key] = int(book[key])

    for key in big_int_key_lt:
        book[key] = int(float(book[key]))

    for key in float_key_lt:
        book[key] = float(book[key])
  
    for key in str_key_lt:
        book[key] = str(book[key])

    return book


def loadTags(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'GoodReads/tags.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        # model.addTag(catalog, tag)
        model.add_tag(catalog, tag)
    # return model.tagSize(catalog)
    return model.tags_size(catalog)


def loadBooksTags(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    booktagsfile = cf.data_dir + 'GoodReads/book_tags.csv'
    input_file = csv.DictReader(open(booktagsfile, encoding='utf-8'))
    for booktag in input_file:
        # model.addBookTag(catalog, booktag)
        model.add_book_tag(catalog, booktag)
    # return model.bookTagSize(catalog)
    return model.book_tags_size(catalog)


# Funciones de ordenamiento
def sortBooks(catalog):
    """
    Ordena los libros por average_rating
    """
    # model.sortBooks(catalog)
    model.sort_books(catalog)


# Funciones de consulta sobre el catálogo

def getBooksByAuthor(control, authorname):
    """
    Retrona los libros de un autor
    """
    # author = model.getBooksByAuthor(control['model'], authorname)
    author = model.get_books_by_author(control['model'], authorname)
    return author


def getBestBooks(control, number):
    """
    Retorna los mejores libros
    """
    # bestbooks = model.getBestBooks(control['model'], number)
    bestbooks = model.get_best_books(control['model'], number)
    return bestbooks


def countBooksByTag(control, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    # return model.countBooksByTag(control['model'], tag)
    return model.count_books_by_tag(control['model'], tag)
