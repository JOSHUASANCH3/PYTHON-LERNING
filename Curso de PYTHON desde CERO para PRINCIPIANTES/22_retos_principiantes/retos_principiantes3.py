# * DIFICULTAD EXTRA (opcional):
# * Crea una agenda de contactos por terminal.
# * - Debes implementar funcionalidades de búsqueda, inserción, actualización
# *   y eliminación de contactos.
# * - Cada contacto debe tener un nombre y un número de teléfono.
# * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
# *   y a continuación los datos necesarios para llevarla a cabo.
# * - El programa no puede dejar introducir números de teléfono no númericos y con más
# *   de 11 dígitos (o el número de dígitos que quieras).
# * - También se debe proponer una operación de finalización del programa.

#! PUNTOS EXTRAS ESTA PARTE SE AÑADE A CURSO INTEMEDIO
#?Retos adicionales (opcionales):
#*Persistencia de datos:
#Guarda la agenda en un archivo (por ejemplo, agenda.txt) para que los contactos no se pierdan al cerrar el programa.
#Usa el módulo json para guardar y cargar los datos en formato JSON.

#*Interfaz más amigable:
#Usa colores o tablas para mostrar los contactos de manera más organizada.

#*Búsqueda avanzada:
#Permite buscar contactos por parte del nombre (por ejemplo, buscar "Ju" para encontrar "Juan").

## Se creara una clase para el control de datos
class Agenda:
    #? Se define el contructor de la clase
    def __init__(self, contactos_iniciales=None):
        #? Se verifica el diccionario
        if contactos_iniciales is None:
            self._contactos = {}  # Diccionario privado para almacenar los contactos
        else:
            self._contactos = contactos_iniciales

    #?Getter para el diccionario de contactos
    @property
    def contactos(self):
        #? Getter para obtener el diccionario de contactos
        return self._contactos

    #? Setter para el diccionario de contactos
    @contactos.setter
    def contactos(self,nuevos_contactos):
        if isinstance(nuevos_contactos, dict):
            self._contactos = nuevos_contactos
        else:
            raise ValueError("Los contactos deben ser diccionarios")
        
    #? Metodo para agregar contactos
    def agregar_contacto(self,nombre, apellido, email, direccion, telefono):
        if nombre in self._contactos:
            print(f"El contacto '{nombre}' ya existe.")
        elif not telefono.isdigit() or len(telefono) > 11:
            print("El numero no es valido, tiene que ser menos de 11 caracteres")
        else:
            self._contactos[nombre] = {
                "Nombre": nombre,
                "Apellido":apellido,
                "Email":email,
                "Direccion":direccion,
                "Teléfono": telefono
            }
            print("El contacto se ha agregado correctamente")

    #? Metodo para actualizar contacto
    def actualizar_contacto(self, nombre, nuevo_telefono):
        #? Actualiza el contacto conforme el nombre
        if nombre in self._contactos:
            self._contactos[nombre] = nuevo_telefono
            print(f"Contacto '{nombre}' actualizado correctamente.")
        else:
            print(f"El contacto '{nombre}' no existe.")

    #?Una funcion para mostrar los ocntactos
    def mostrar_contactos(self, nombre):
        if nombre in self._contactos:
            print(f"Nombre: {nombre}, Apellido: {self._contactos[nombre]}")
        else:
            print(f"El contacto {nombre} no existe en la agenda")
    
    #? Método para eliminar un contacto
    def eliminar_contacto(self, nombre):
        if nombre in self._contactos:
            del self._contactos[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"El contacto '{nombre}' no existe.")

class_agenda = Agenda()
while True:
    # Mostrar menú
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        # Buscar contacto
        search_contacto = input("Ingrese el nombre del contacto :")
        class_agenda.mostrar_contactos(search_contacto)
        pass
    elif opcion == "2":
        # Insertar contacto
        add_nombre = input("Ingresa el nombre: ")
        add_apellido = input("Ingrese apellido: ")
        add_email = input("Ingrese el correo electronico: ")
        add_direccion = input("Ingrese la dirrecion: ")
        add_numero = input("Ingrese la numero: ")
        class_agenda.agregar_contacto(add_nombre, add_apellido, add_email, add_direccion, add_numero)
        pass
    elif opcion == "3":
        #Actualizar contacto
        act_contacto = input("Escriba el nombre del contacto a actualizar")
        class_agenda.actualizar_contacto(act_contacto)
        pass
    elif opcion == "4":
        # Eliminar contacto
        del_contacto = input("Escriba el nombre del contacto a eliminar")
        class_agenda.eliminar_contacto(del_contacto)
        pass
    elif opcion == "5":
        # Salir del programa
        print("Has salido")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")