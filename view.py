# Purpose: Vista del programa
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    """
    Menu de usuario
    """
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x libros por promedio")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("0- Salir")


def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags = controller.loadData(control)
    return books, authors, tags, book_tags


def printAuthorData(author):
    """
    Recorre la lista de libros de un autor, imprimiendo
    la informacin solicitada.
    """
    if author:
        # print(author)
        # print('Autor encontrado: ' + author['name'])
        # print('Promedio: ' + str(author['average_rating']))
        # print('Total de libros: ' + str(lt.size(author['books'])))
        print('Total de libros: ' + str(author.size()))
        
        # for book in lt.iterator(author['books']):
        for book in author:
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


def printBestBooks(books):
    """
    Imprime los mejores libros solicitados
    """
    size = books.size()
    if size:
        print(' Estos son los mejores libros: ')
        # for book in lt.iterator(books):
        for book in books:
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
    else:
        print('No se encontraron libros')


# Se crea el controlador asociado a la vista
control = newController()


# main del ejercicio
if __name__ == "__main__":

    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = loadData(control)
            print('Libros cargados: ' + str(bk))
            print('Autores cargados: ' + str(at))
            print('Géneros cargados: ' + str(tg))
            print('Asociación de Géneros a Libros cargados: ' +
                  str(bktg))

        elif int(inputs[0]) == 2:
            number = input("Buscando los TOP ?: ")
            books = controller.getBestBooks(control, int(number))
            printBestBooks(books)

        elif int(inputs[0]) == 3:
            authorname = input("Nombre del autor a buscar: ")
            author = controller.getBooksByAuthor(control, authorname)
            printAuthorData(author)

        elif int(inputs[0]) == 4:
            label = input("Etiqueta a buscar: ")
            book_count = controller.countBooksByTag(control, label)
            print('Se encontraron: ', book_count, ' Libros')

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)
