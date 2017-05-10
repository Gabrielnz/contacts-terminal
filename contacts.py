


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        # si el ciclo se ejecuta y no encuentra el nombre
        else:
            self._not_found()

    def delete(self, name):
        # con enumerate obtenemos el indice del contacto, ademas del contacto en si
        for i, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[i]
                break
        # si el ciclo se ejecuta y no encuentra el nombre
        else:
            self._not_found()

    def _not_found(self):
        print('**********')
        print('¡No encontrado!')
        print('**********')


def run():

    contact_book = ContactBook()

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))

            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()