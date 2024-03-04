# El código define una clase Componente que tiene un atributo privado __atributo. Se utilizan los decoradores @property y @atributo.setter para crear métodos getter y setter para este atributo.
#
# El método getter atributo permite acceder al valor del atributo de forma segura desde fuera de la clase.
# El método setter atributo valida cualquier nuevo valor asignado al atributo antes de actualizarlo. En este caso, solo se permite asignar valores enteros positivos al atributo.
# Luego, se instancia un objeto de la clase Componente con un valor inicial de 10. Se realizan varias operaciones de asignación de valores al atributo atributo, mostrando cómo funciona la validación en el setter y cómo se accede al atributo a través del getter.
class Componente:
    def __init__(self, atributo):
        self.__atributo = atributo  # Inicializa el atributo privado con el valor proporcionado

    @property
    def atributo(self):  # Getter para el atributo
        return self.__atributo

    @atributo.setter  # Setter para el atributo
    def atributo(self, nuevo_atributo):
        if nuevo_atributo > 0 and isinstance(nuevo_atributo, int):
            self.__atributo = nuevo_atributo  # Actualiza el atributo privado si el nuevo valor es un entero positivo
        else:
            print(
                "Por favor, ingrese un valor entero positivo para el atributo")  # Mensaje de error si se intenta establecer un valor no válido


componente = Componente(10)
print(componente.atributo)  # Imprime el valor inicial del atributo

componente.atributo = -1  # Intenta establecer un valor negativo para el atributo
print(
    componente.atributo)  # Imprime el valor actualizado del atributo, que no cambió debido a la validación en el setter

componente.atributo = 20  # Intenta establecer un valor válido para el atributo
print(componente.atributo)  # Imprime el valor actualizado del atributo

componente.atributo = 3.5  # Intenta establecer un valor no entero para el atributo
print(
    componente.atributo)  # Imprime el valor actualizado del atributo, que no cambió debido a la validación en el setter

# El decorador @property permite definir un método como un atributo de solo lectura, lo que significa que puede ser accedido como un atributo sin llamar explícitamente a un método. Por otro lado, @atributo.setter permite definir un método que se ejecuta cada vez que se intenta asignar un valor al atributo correspondiente. Esto proporciona una manera de validar y controlar la asignación de valores a los atributos de la clase. En este caso, se utiliza para asegurarse de que el atributo sea un entero positivo.
