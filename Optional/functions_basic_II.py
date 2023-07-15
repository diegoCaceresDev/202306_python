#Cuenta regresiva

def cuenta_regresiva(num):
  cuenta= []
  for i in range(num, 0, -1):
    cuenta.append(i)
  return cuenta

print(cuenta_regresiva(10))

#Imprimir y devolver

def imprimir_y_devolver(imprimir, devolver):
  print(imprimir)
  return devolver

print(imprimir_y_devolver(10, 5))

#Primero más longitud

def primero_mas_longitud(list):
  return (list[0] + len(list))

print(primero_mas_longitud([5,1,3,5]))

#Valores mayores que el segundo

def mayor_del_segundo(list):
  newList= []
  if (len(list) < 2):
    return False
  
  for x in list:
    if(x > list[1]):
      newList.append(x)
  
  return newList

print(mayor_del_segundo([1, 4, 5, 2, 8]))
print(mayor_del_segundo([1]))

#Esta longitud, ese valor

def longitud_y_valor(longitud, valor):
  newList = []

  for x in range(longitud):
    newList.append(valor)

  return newList

print(longitud_y_valor(5, 7))
print(longitud_y_valor(8, 3))
