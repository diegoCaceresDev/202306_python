#1 Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

#Ejercicio1 Actualizar valores en diccionarios y listas

#1 Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

x[1][0]= 15
print(x)

#2 Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

estudiantes[0]["last_name"] = "Bryant"
print(estudiantes)

#3 En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes['fútbol'][0] = "Andres"
print(directorio_deportes)

#4 Cambia el valor 20 en z a 30.

z[0]["y"]= 30
print(z)

print("-"*40)
#Ejercicio2 - Iterar a través de una lista de diccionarios

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in some_list:
      print(x)

iterateDictionary(estudiantes)

#Ejercicio3 Obtener valores de una lista de diccionarios
 
def iterateDictionary2(key_name, some_list):
  for estudiantes in some_list:
     print(some_list)










