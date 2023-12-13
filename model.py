# nueva implementacion
from DISClib.ADT.lists import List
from DISClib.ADT.lists import clone
from DISClib.ADT.lists import translate
# from DISClib.ADT.queue import Queue
# from DISClib.ADT.stack import Stack
# from DISClib.ADT.maps import Map

# antigua implementacion
# import config as cf
# from DISClib.ADT import list as lt
# from DISClib.Algorithms.Sorting import shellsort as sa
# assert cf

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores
y otra para géneros
"""

# Construccion de modelos


def new_catalog() -> dict:
    """newCatalog _summary_

    Returns:
        dict: _description_
    """ 
    
    catalog = {
        "books": None,
        "authors": None,
        "tags": None,
        "book_tags": None
    }
    
    catalog["books"] = List(dstruct="ArrayList")
    catalog["authors"] = List(dstruct="SingleLinked",
                              cmp_function=cmp_authors)
    catalog["tags"] = List(dstruct="SingleLinked",
                            cmp_function=cmp_tag_names)
    catalog["book_tags"] = List()
    return catalog


# funciones para comparar elementos dentro de las listas
def cmp_authors(author_name1:str, author2:dict) -> int:
    """cmp_authors _summary_

    Args:
        author1 (dict): _description_
        author2 (dict): _description_

    Returns:
        int: _description_
    """  
    if author_name1.lower() == author2["name"].lower():
        return 0
    elif author_name1.lower() > author2["name"].lower():
        return 1
    return -1


def cmp_tag_names(tag_name1:str, tag2:dict) -> int:
    """cmp_tag_names _summary_

    Args:
        tag_name1 (dict): _description_
        tag2 (dict): _description_

    Returns:
        int: _description_
    """
    print(tag_name1, tag2)
    if tag_name1 == tag2["name"]:
        return 0
    elif tag_name1 > tag2["name"]:
        return 1
    return -1


# Funciones para agregar informacion al catalogo
def add_book(catalog:dict, book:dict) -> dict:
    """add_book _summary_

    Args:
        catalog (dict): _description_
        book (dict): _description_

    Returns:
        dict: _description_
    """ 
    # TODO add docstring
    books_lt = catalog["books"]
    books_lt.add_last(book)
    book_author_lt = book["authors"].split(",")
    for author in book_author_lt:
        add_book_author(catalog, author.strip(), book)
    return catalog

# def addBook(catalog, book):
#     # Se adiciona el libro a la lista de libros
#     lt.addLast(catalog['books'], book)
#     # Se obtienen los autores del libro
#     authors = book['authors'].split(",")
#     # Cada autor, se crea en la lista de libros del catalogo, y se
#     # crea un libro en la lista de dicho autor (apuntador al libro)
#     for author in authors:
#         addBookAuthor(catalog, author.strip(), book)
#     return catalog

def add_book_author(catalog:dict, author_name:str, book:dict) -> dict:
    """add_book_author _summary_

    Args:
        catalog (dict): _description_
        author_name (str): _description_
        book (dict): _description_

    Returns:
        dict: _description_
    """
    # TODO add docstring
    authors_lt = catalog["authors"]
    idx_author = authors_lt.find(author_name)
    if idx_author > -1:
        author = authors_lt.get_element(idx_author)
    else:
        author = new_author(author_name)
        authors_lt.add_last(author)
    author["books"].add_last(book)
    return catalog

def addBookAuthor(catalog, authorname, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['books'], book)
    return catalog


def add_tag(catalog:dict, tag:dict) -> dict:
    """add_tag _summary_

    Args:
        catalog (dict): _description_
        tag (dict): _description_

    Returns:
        dict: _description_
    """
    # TODO add docstring
    tag = new_tag(tag["tag_name"],
                  tag["tag_id"])
    catalog["tags"].add_last(tag)
    return catalog


# def addTag(catalog, tag):
#     """
#     Adiciona un tag a la lista de tags
#     """
#     t = newTag(tag['tag_name'], tag['tag_id'])
#     lt.addLast(catalog['tags'], t)
#     return catalog


def add_book_tag(catalog:dict, book_tag:dict) -> dict:
    """add_book_tag _summary_

    Args:
        catalog (dict): _description_
        book_tag (dict): _description_

    Returns:
        dict: _description_
    """  
    # TODO add docstring
    book_tag = new_book_tag(book_tag["tag_id"],
                            book_tag["goodreads_book_id"])
    catalog["book_tags"].add_last(book_tag)
    return catalog

# def addBookTag(catalog, booktag):
#     """
#     Adiciona un tag a la lista de tags
#     """
#     t = newBookTag(booktag['tag_id'], booktag['goodreads_book_id'])
#     lt.addLast(catalog['book_tags'], t)
#     return catalog


# Funciones para creacion de datos

def new_author(author_name:str) -> dict:
    """new_author _summary_

    Args:
        author_name (str): _description_

    Returns:
        dict: _description_
    """
    # TODO add docstring
    author = {
        "name": "",
        "books": None,
        "average_rating": 0,
    }
    author["name"] = author_name
    author["books"] = List(dstruct="ArrayList")
    return author


# def newAuthor(name):
#     """
#     Crea una nueva estructura para modelar los libros de
#     un autor y su promedio de ratings
#     """
#     author = {'name': "", "books": None,  "average_rating": 0}
#     author['name'] = name
#     author['books'] = lt.newList('ARRAY_LIST')
#     return author


def new_tag(tag_name:str, tag_id:str) -> dict:
    """new_tag _summary_

    Args:
        tag_name (str): _description_
        tag_id (str): _description_

    Returns:
        dict: _description_
    """
    # TODO add docstring
    tag = {
        "name": "",
        "tag_id": ""
    }
    tag["name"] = tag_name
    tag["tag_id"] = tag_id
    return tag


# def newTag(name, id):
#     """
#     Esta estructura almancena los tags utilizados para marcar libros.
#     """
#     tag = {'name': '', 'tag_id': ''}
#     tag['name'] = name
#     tag['tag_id'] = id
#     return tag


def new_book_tag(tag_id:str, book_id:str) -> dict:
    """new_book_tag _summary_

    Args:
        tag_id (str): _description_
        book_id (str): _description_

    Returns:
        dict: _description_
    """  
    # TODO add docstring
    book_tag = {
        "tag_id": "",
        "book_id": "",
    }
    book_tag["tag_id"] = tag_id
    book_tag["book_id"] = book_id
    return book_tag


# def newBookTag(tag_id, book_id):
#     """
#     Esta estructura crea una relación entre un tag y
#     los libros que han sido marcados con dicho tag.
#     """
#     booktag = {'tag_id': tag_id, 'book_id': book_id}
#     return booktag


# Funciones de consulta


def get_books_by_author(catalog:dict, author_name:str) -> List:
    """get_books_by_author _summary_

    Args:
        catalog (dict): _description_
        author_name (str): _description_

    Returns:
        List: _description_
    """
    # TODO add docstring
    authors_lt = catalog["authors"]
    idx_author = authors_lt.find(author_name)
    if idx_author > -1:
        author = authors_lt.get_element(idx_author)
        return author["books"]
    return None



# def getBooksByAuthor(catalog, authorname):
#     """
#     Retorna un autor con sus libros a partir del nombre del autor
#     """
#     posauthor = lt.isPresent(catalog['authors'], authorname)
#     if posauthor > 0:
#         author = lt.getElement(catalog['authors'], posauthor)
#         return author
#     return None


def get_best_books(catalog:dict, number:int) -> List:
    """get_best_books _summary_

    Args:
        catalog (dict): _description_
        number (int): _description_

    Returns:
        List: _description_
    """
    # TODO add docstring
    books_lt = catalog["books"]
    best_books_lt = List()
    i = 0
    for book in books_lt:
        if i < number:
            best_books_lt.add_last(book)
            i += 1
        # best_books_lt.add_last(book)
    
    return best_books_lt


# def getBestBooks(catalog, number):
#     """
#     Retorna los mejores libros
#     """
#     books = catalog['books']
#     bestbooks = lt.newList()
#     for cont in range(1, number+1):
#         book = lt.getElement(books, cont)
#         lt.addLast(bestbooks, book)
#     return bestbooks


def count_books_by_tag(catalog:dict, tag:str) -> int:
    """count_books_by_tag _summary_

    Args:
        catalog (dict): _description_
        tag (str): _description_

    Returns:
        int: _description_
    """
    # TODO add docstring
    tags_lt = catalog["tags"]
    book_tags_lt = catalog["book_tags"]
    book_count = 0
    idx_tag = tags_lt.find(tag)
    if idx_tag > 0:
        tag = tags_lt.get_element(idx_tag)
        for book_tag in book_tags_lt:
            if book_tag["tag_id"] == tag["tag_id"]:
                book_count += 1        
    return book_count


# def countBooksByTag(catalog, tag):
#     """
#     Retorna los libros que fueron etiquetados con el tag
#     """
#     tags = catalog['tags']
#     bookcount = 0
#     pos = lt.isPresent(tags, tag)
#     if pos > 0:
#         tag_element = lt.getElement(tags, pos)
#         if tag_element is not None:
#             for book_tag in lt.iterator(catalog['book_tags']):
#                 if tag_element['tag_id'] == book_tag['tag_id']:
#                     bookcount += 1
#     return bookcount


def books_size(catalog:dict) -> int:
    """books_size _summary_

    Args:
        catalog (dict): _description_

    Returns:
        int: _description_
    """
    # TODO add docstring
    books_lt = catalog["books"]
    return books_lt.size()


def authors_size(catalog:dict) -> int:
    """authors_size _summary_

    Args:
        catalog (dict): _description_

    Returns:
        int: _description_
    """
    # TODO add docstring
    authors_lt = catalog["authors"]
    return authors_lt.size()


def tags_size(catalog:dict) -> int:
    """tags_size _summary_

    Args:
        catalog (dict): _description_

    Returns:
        int: _description_
    """    
    # TODO add docstring
    tags_lt = catalog["tags"]
    return tags_lt.size()


def book_tags_size(catalog:dict) -> int:
    """book_tags_size _summary_

    Args:
        catalog (dict): _description_

    Returns:
        int: _description_
    """
    # TODO add docstring
    book_tags_lt = catalog["book_tags"]
    return book_tags_lt.size()


# def bookSize(catalog):
#     return lt.size(catalog['books'])


# def authorSize(catalog):
#     return lt.size(catalog['authors'])


# def tagSize(catalog):
#     return lt.size(catalog['tags'])


# def bookTagSize(catalog):
#     return lt.size(catalog['book_tags'])


# Funciones utilizadas para comparar elementos dentro de una lista

# def compareauthors(authorname1, author):
#     if authorname1.lower() == author['name'].lower():
#         return 0
#     elif authorname1.lower() > author['name'].lower():
#         return 1
#     return -1


# def comparetagnames(name, tag):
#     if (name == tag['name']):
#         return 0
#     elif (name > tag['name']):
#         return 1
#     return -1


# funciones para comparar elementos dentro de algoritmos de ordenamientos

def rating_criteria(book1:dict, book2:dict) -> bool:
    """rating_criteria _summary_

    Args:
        book1 (dict): _description_
        book2 (dict): _description_

    Returns:
        bool: _description_
    """    
    return (float(book1["average_rating"]) > float(book2["average_rating"]))

def sort_books(catalog:dict) -> dict:
    """sort_books _summary_

    Args:
        catalog (dict): _description_

    Returns:
        dict: _description_
    """    
    # TODO add docstring
    books_lt = catalog["books"]
    sa.sort(books_lt, rating_criteria)
    return catalog

# def compareratings(book1, book2):
#     return (float(book1['average_rating']) > float(book2['average_rating']))


# # Funciones de ordenamiento

# def sortBooks(catalog):
#     sa.sort(catalog['books'], compareratings)
