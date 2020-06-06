# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Filosofía de python
import this

print('Hola Mundo')
print("Hola Mundo")

# Comentario de linea
# Comentario de linea 2
# Comentario de linea 3
"""
Comentario
De 
varias
Lineas
"""
'''
Comentario
De
varias
Lineas
'''

# Variables

numero = 3
type(numero)
numero = 3.0
type(numero)
numero = "3.0"
type(numero)

# forma correcta declarar variables

numero = 3
numero_uno=3
_numero_uno = 3
numeroUno = 3
NUMEROUNO=3
numero1 = 3

# forma incorrecta de variables

1numero = 3
numero-uno = 3
numero uno=3

numero = 3
Numero = 3

# Asignación

x = 1
y = 2
z = 3

x, y, z = 1, 2, 3
a = b = c = d = 1

NUMERO = 3

# Tipo de datos básicos

texto = 'hola' # str
numero = 4     # int
decimal = 4.5 # float
booleano = True # bool
booleano = False # bool
complejo = 4+3j # complex
a = None # None

# Conversión implícita

a = 4 + 2 #int
b = 4 + 2.0 # float
a = 'hola' * 2 #str
a = 5 + True # int

# Conversión explícita tipos básicos

a = 5;
b = str(a)
c = float(a)
a = int(b)
d = complex(b)

# Operaciones

suma = 3 + 4
resta = 2 - 4
mult = 3 * 2
div = 3 / 2
div_dos = 3 // 2
mod = 4 % 2
potencia = 4 ** 2
import math
raiz_cuadrada = math.sqrt(4)
raiz_cubica = 9 ** (1 / 3)

# String

a = 'hola'
a = "hola"
a = "hola"
b = a[2]

c = "   Roberto Morales Ortega  "
nombre = c[0:7] # c[:7]
primer_apellido = c[8:15]
segundo_apellido = c[16:22] # c[16:]
len(c)
b = c.strip()
b.lower()
b.upper()
b.replace("r","c")
b.split()
b.split('r')
'les' in b
'i' not in b
c = a + b
b = 2
c = a + str(b)

a = 'Edad'
b = 5
c = "La 
c = "La {} es {}"
print(c.format(a,b))
print(f'La edad {a} es {b}')

# Booleans

False == 0
True == 1
a == b
a != b
a <= b
a >= b
a < b
a > b


# False en boolean
bool(False)
bool(None)
bool(0)
bool("")
bool('')
bool(())
bool([])
bool({})


# Operadores lógicos

and
or
not

# Operaciones de asignación

a = 5
a += 5 # a = a + 5
a -= 5 # a = a - 5
a *= 5 # a = a * 5
a/= 5 # a = a / 5
a //= 5 # a = a // 5
a %= 5 # a = a % 5
a **= 5 # a = a ** 5


# Operador de identidad
is
is not

# Operador de contenido
in
not in

# input y output

a = input('Digita tu nombre: ')
print(a)

num_uno = int(input('Digite el número uno: '))
num_dos = int(input('Digite el número dos: '))

suma = num_uno + num_dos
print(f'La suma es: {suma}')

# Listas
# Tipos de datos mutables y ordenados

a = [4, 5, 6]
print(a[0])
a[2]=7
a = [4, 4.5, 'hola', 4j]
a.append(6)
b = copy(a)
b = a[::]
a[-1]
a.remove(8) #Elimina el elemento por el valor
a.pop() # Elimina el último elemento
a.pop(-2) #Elimina el elemento por posición
del a
a.clear()
4 in a
len(a)
c= a + b #Concatena 

# Tuplas
# Tipos de datos inmutables y ordenados
a = (4, 5, 6)
a=(4,5,6,'hola')
a[0]
a[0:2]
4 in a
len(a)
del a
c= a + b #Concatena 
a = (500,)

# set
# Tipos de datos mutable y no ordenado
# Ordena de menor a mayor
# no permite valores repetidos

c = {5, 6, 7}
c.add('Hola')
c.update([6,7,8])
c.remove(5) # muestra error al no entrar el elemento
c.discard(5) #no muestra error al no encontrar el elemento
c.pop()
c.clear()

# Conversiones
a = [4, 5, 6]
b = set(a)
b = tuple(a)
a= list(b)

# Dictionario

# Tipo de dato mutable y no ordenado

diccionario = {'nombre':'Roberto', 
       'apellido': 'Morales'}
diccionario_dos = {'a': 1, 'b': 2}
diccionario_tres = {1: 'a', 2: 'b'}
diccionario['nombre']
diccionario.get('nombre')
diccionario['nombre'] = 'Carlos'
diccionario.values()
dict_keys(['nombre', 'apellido'])
'apellido' in diccionario # busca solo dentro de las llaves
'Morales' in diccionario.values()
len(diccionario)
diccionario['estado_civil'] = 'Casado'
diccionario.pop('estado_civil')
diccionario.popitem()
diccionario.clear()
del diccionario
diccionario.copy()

# Diccionario Anidado

diccionario = {
        'nombre':'Roberto', 
       'apellido': 'Morales',
       'hobbies':{
               'nombre': 'Jugar futbol',
               'frecuencia':'ocasional'
               }
       }

diccionario_uno = {'nombre':'Roberto', 
       'apellido': 'Morales'}

diccionario_dos = {'nombre':'Carlos', 
       'apellido': 'Perez'}

vec_diccionarios = [diccionario_uno, diccionario_dos]


# Booleans

False == 0
True == 1
a == b
a != b
a <= b
a >= b
a < b
a > b


# False en boolean
bool(False)
bool(None)
bool(0)
bool("")
bool('')
bool(())
bool([])
bool({})


# Operadores lógicos

and
or
not

# Sentencia if

if 4 == 4:
    print('Es igual')
print('Está fuera del if')

if 4 == 4 and 4 <= 5:
    print('Es igual')
print('Está fuera del if')


if 4 == 4:
    print('Es igual')
else:
    print('Es diferente')


if 4 == 4:
    print('x')
elif 5 ==7:
    print('y')
elif 8 == 4:
    print('z')
else:
    print('p')

if 4 == 4:
    if 7== 7:
        print('z')
        print('x')
elif (5 ==7):
    print('y')
elif 8 == 4:
    print('z')
else:
    print('p')

# Sentencia for
a = [4,5,6]
a = (4,5, 6)
a = {4, 5, 6}

for valor in a:
    print(valor)
    print(valor + 2)
    print(valor * 5)
    
for valor in a:
    print (valor)
    
for valor in a.keys():
    print (valor)

for valor in a.values():
    print (valor)
    
for valor in a.items():
    print (f'{valor[0]}: {valor[1]}')

for llave, valor in a.items():
    print (f'{llave.capitalize()}: {valor}')
    
for llave, valor in a.items():
    print (f'{llave.upper()}: {valor}')
    

for valor in range(1,11):
    print (valor)

for valor in range(2,11, 2):
    print (valor, end=',')
    
for valor in range(2,11, 2):
    print (valor, end=',')
    
for valor in list(range(1,11)):
    print (valor)
    
# Sentencia While

i=1
while 1:
    print(i)
    i+= 1

# Funciones 
    
def nombre_funcion():
    pass

def hola_mundo():
    print('Hola Mundo')
    
def hola_mundo(nombre):
    print(f'Hola {nombre}')
    
def hola_mundo(nombre='Mundo'):
    print(f'Hola {nombre}')
    
def hola_mundo(nombre='Mundo'):
    print(f'Hola {nombre}')

def sumar(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    print(f'La suma de {numero_uno} con {numero_dos} es {suma}')
    
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""

def sumar(numero_uno, numero_dos):
    """
    Se realiza la suma de dos números.
    
    Args:
        numero_uno: primer número a sumar
        numero_dos: segundo número a sumar
    
    Returns:
        Se devuelve la suma de los números    
    """
    suma = numero_uno + numero_dos
    return suma

def restar(numero_uno, numero_dos):
    """ Resta dos números """
    resta = numero_uno - numero_dos
    return resta

sumar(4,5) # invocar un método por posición
sumar(numero_dos=5, numero_uno=4) # invocar por asignación

def operar(numero_uno, numero_dos):
    suma = sumar(numero_uno, numero_dos)
    resta = restar(numero_uno, numero_dos)
    return suma, resta

res_sum, res_res = operar(4,5)
resultado = operar(4,5)

# recibir cantidad indeterminada de argumentos
def test(*args):
    for valor in args:
        print(valor)

def test(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

# Clases y objetos en Python
        
class Persona:
    
    __cedula = ""
    
    #Constructor
    def __init__(self, cedula, nombre, apellido):
        self.__cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        
    # Metodos
    def saludar(self):
        print(f'Hola {self.nombre} {self.apellido}')
    
    def reir(self):
        print(f'jajaja {self.nombre}')


p = Persona('1143234567', 'Sergio', 'Perez')
p.nombre='Carlos'
p.saludar()















