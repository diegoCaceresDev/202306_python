# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Diego"
print("Hola,", name)	# con una coma
print("Hola, " + name)	# con un +
print(f"Hola, {name}")
# 3. imprimir "Hola 42!" con el número en una variable
num = 42
print("Hola", num, "!")	# con una coma
print("Hola " + str(num) + "!")	# con una +	-- este debería arrojar un error!
print(f"Hola {num}!")
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}".format(fave_food1, fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

#bonus
print("Hola, mundo".lower())
print("Hola, mundo".upper())
print("Hola, mundo".replace(" ", ""))
print("Hola, mundo".split(","))




