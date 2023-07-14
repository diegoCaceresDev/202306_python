#- Data Types
# Primitive
num1 = 42  #Numbers
num2 = 2.3  #Numbers
boolean = True #Boolean
string = 'Hello World' #Strings
# Composite
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # - variable declaration -List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # - variable declaration -Dictionary 

fruit = ('blueberry', 'strawberry', 'banana') # - variable declaration -Tuples 
print(type(fruit)) #- type check
print(pizza_toppings[1]) # list - access value
pizza_toppings.append('Mushrooms') # list - add value
print(person['name']) # dictionary - access value
person['name'] = 'George' # dictionary - change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # tuple - access value

#conditional
if num1 > 45:
    print("It's greater") 
else:
    print("It's lower")
    
#conditional
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    
#for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
    
# while loop
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #list - delete value
pizza_toppings.pop(1) #list - delete value

print(person) #dictionary - access value
person.pop('eye_color') #dictionary - delete value
print(person) #dictionary - access value

    #for loop
for topping in pizza_toppings:
    #conditional start
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #stop

#- function
def print_hello_ten_times( ):#parameter
    for num in range(10): #- argument
        print('Hello')

print_hello_ten_times()

#- function
def print_hello_x_times(x): #parameter
    for num in range(x):#- argument
        print('Hello')

print_hello_x_times(4)

#- function
def print_hello_x_or_ten_times(x = 10): #parameter
    for num in range(x):#- argument
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)