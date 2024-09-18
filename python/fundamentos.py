from funciones import nuevo_Tema, nuevo_subtema


print("Hola Mundo mi nombres es 'Denisse'")
print('Saludos')
 


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else: 
        return n * factorial (n - 1)
numero = 5
print('factorial de', numero, 'es', factorial(numero))


nuevo_Tema('variables')
numero = 5
print('numero: ', numero)

edad = 20
print('edad: ',edad)

altura = 1.85
print('altura: ',altura)

nombre = 'Eliud'
print('nombre: ',nombre)

es_trabajador = True 
print('es_tra: ',es_trabajador)




nuevo_Tema('Listas')

frutas = ['manzanas', 'peras', 'piñas', 'naranjas', 'guayabas', 'papayas']
print('frutas:', frutas)

varias_cosas = ['Escuela', 23, True, frutas]
print('varias_cosas', varias_cosas)

#Seleccionando un elemento
print('frutas[0]:', frutas[0])

print('frutas[-2]:', frutas[-2])

print('frutas[1:5]:', frutas[1:5])
print('frutas[1:5:2]:', frutas[1:5:2])

#agregando un elemento al final
frutas.append('fresas') #agregamos 
print('frutas:', frutas)
#eliminando un elemnto
frutas.remove('naranjas') #quitamos
print('frutas:', frutas)

#insertar elemento en la posición descrita
frutas.insert(4, 'kiwi') #inserta en la posición 
print('frutas:', frutas)

#creando una lista vacia
calificaciones = []
Libros = list() #otro modo de genera lista vacia
print('Libros:', Libros)
print('calificaciones:', calificaciones)

frutas.reverse()
print("frutas: ", frutas)
frutas.sort()
print("frutas: ", frutas)

nuevo_Tema("diccionarios")

persona={"nombre": "pedro", 
         "apellido": "Pérez", 
         "edad": 48 , 
         "estatura": 1.70 , 
         "hijos": ["Casimira", "Brayan", "Eliud"]}

print('persona: ', persona)

print ("persona.keys(): ", persona.keys())
print ("persona.values(): ", persona.values())

print ('persona.get("nombre"): ', persona.get("nombre"))
print ('persona.get("estatura"): ', persona.get("estatura"))

print ('persona.items(): ', persona.items()) #items significa dame todos los elemtentos


nuevo_Tema ("Ciclos")
nuevo_subtema ("for")
for i in range (10):
    print (i)

print("#######")
for i in range (3,10):
    print(i)

print("#######")
for i in range (3,10, 2):
    print (i)

print ("len(frutas) :", len(frutas)) #longitudad/cantidad de elementos

for fruta in frutas:
    print(fruta)

print ("######### con len")
for indice in range(len(frutas)):
    print ("indice, ",indice, frutas [indice])
print ("######### con enumerate")
for indice, fruta in enumerate(frutas): #enumeracion de los elementos
    print (indice, fruta)

for key, value in persona.items(): #dos variables en una
    print (key, value)


