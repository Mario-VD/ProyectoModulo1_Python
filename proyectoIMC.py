# Creado por: Mario Alberto Valverde Díaz (marzo, 2024)


# Solicitar los datos general del usario y darles un formato apropiado.
nombre = input("Ingrese su nombre: ").capitalize()  # Solicita el nombre del usuario y pone la primera letra en mayúscula
while not nombre.strip():  # Verifica si el nombre está vacío o contiene solo espacios en blanco
    print("No ha ingresado el nombre.")  # Imprime un mensaje de error si el nombre está vacío o contiene solo espacios en blanco
    nombre = input("Ingrese su nombre: ").capitalize()  # Solicita nuevamente el nombre del usuario y pone la primera letra en mayúscula

apellido_paterno = input("Ingrese su apellido paterno: ").capitalize()  # Solicita el apellido paterno del usuario y pone la primera letra en mayúscula
while not apellido_paterno.strip():  # Verifica si el apellido paterno está vacío o contiene solo espacios en blanco
    print("No ha ingresado el apellido paterno.")  # Imprime un mensaje de error si el apellido paterno está vacío o contiene solo espacios en blanco
    apellido_paterno = input("Ingrese su apellido paterno: ").capitalize()  # Solicita nuevamente el apellido paterno del usuario y pone la primera letra en mayúscula

apellido_materno = input("Ingrese su apellido materno: ").capitalize()  # Solicita el apellido materno del usuario y pone la primera letra en mayúscula
while not apellido_materno.strip():  # Verifica si el apellido materno está vacío o contiene solo espacios en blanco
    print("No ha ingresado el apellido materno.")  # Imprime un mensaje de error si el apellido materno está vacío o contiene solo espacios en blanco
    apellido_materno = input("Ingrese su apellido materno: ").capitalize()  # Solicita nuevamente el apellido materno del usuario y pone la primera letra en mayúscula

edad = input("Ingrese su edad: ")  # Solicita la edad del usuario
while not edad.isdigit():  # Verifica si la edad ingresada no es un número entero
    print("La edad debe ser un número entero.")  # Imprime un mensaje de error si la edad no es un número entero
    edad = input("Ingrese su edad: ")  # Solicita nuevamente la edad del usuario
edad = int(edad) # Convierte la edad a un entero

peso = input("Ingrese su peso en kilogramos: ")  # Solicita el peso del usuario en kilogramos
while not peso.replace('.', '', 1).isdigit():  # Verifica si el peso ingresado no es un número decimal
    print("El peso debe ser un número.")  # Imprime un mensaje de error si el peso no es un número
    peso = input("Ingrese su peso en kilogramos: ")  # Solicita nuevamente el peso del usuario en kilogramos
peso = round(float(peso), 1) # Convierte el peso a un número redondeado a un decimal

estatura = input("Ingrese su estatura en metros: ")  # Solicita la estatura del usuario en metros
while not estatura.replace('.', '', 1).isdigit():  # Verifica si la estatura ingresada no es un número decimal
    print("La estatura debe ser un número.")  # Imprime un mensaje de error si la estatura no es un número
    estatura = input("Ingrese su estatura en metros: ")  # Solicita nuevamente la estatura del usuario en metros
estatura = round(float(estatura), 2) # Convierte la estatura a un número  redondeado a dos decimales

# Calcular el IMC (Índice de Masa Corporal)
imc = round(peso / (estatura ** 2), 2)

# Determinar la condición de la persona según su IMC
if imc < 18.5:
    condicion = "Peso Bajo"
elif 18.5 <= imc < 25:
    condicion = "Peso Normal"
elif 25 <= imc < 30:
    condicion = "Sobrepeso"
elif 30 <= imc < 35:
    condicion = "Obesidad Leve"
elif 35 <= imc < 40:
    condicion = "Obesidad Media"
else:
    condicion = "Obesidad Mórbida"

# Mostrar los resultados
print("\n* * * * * * * * * * * * * * * * * * * * ")
print("DATOS DEL USUARIO")
print("Nombre completo:", nombre, apellido_paterno, apellido_materno)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")
print("- - - - - - - - - - - - - - - - - - - - ")
print("ÍNDICE DE MASA CORPORAL")
print("Índice de Masa Corporal (IMC):", imc)
print("Condición de la persona:", condicion)
print("* * * * * * * * * * * * * * * * * * * * ")
