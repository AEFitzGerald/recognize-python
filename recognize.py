num1 = 42 #- variable declaration - Primitive - Number initialized
num2 = 2.3 #- variable declaration - Primitive - Float initialized
boolean = True # Primitive - Boolean Initialized
string = 'Hello World' #  Primitive - String Initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Composite Lists, Initialized, ordered / index begins at 0 / changeable
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Composite Dictionary, Initialized stores values in key:value pairs
fruit = ('blueberry', 'strawberry', 'banana') # Composite Tuples store multiple items in a single variable / ordered and unchangeable 
#/index begins at 0 / one item tuple gets a comma after
print(type(fruit)) # type() function returns the type of the object if looking to the preceedind object, it would return 'tuple'
print(pizza_toppings[1]) # Composite Dictionary access value 
pizza_toppings.append('Mushrooms') #Dictionary change value
print(person['name']) # Composite Dictionary access value
person['name'] = 'George' # Composite Dictionary change/add value
person['eye_color'] = 'blue' #- Composite Dictionary change/add value 
print(fruit[2]) # Composite tuple access value # return index of 2 in the List fruit

if num1 > 45: #- conditional if else
    print("It's greater") # return 
else: #conditional else
    print("It's lower") # return 

if len(string) < 5: # conditional if 
    print("It's a short word!")  #not returned
elif len(string) > 15: # conditional else if 
    print("It's a long word!") # not returned
else: #conditional else
    print("Just right!") #return

for x in range(5): #for loop Start, parameter/arguments
    print(x) #return
for x in range(2,5): #for loop, range function, start 2, end 5
    print(x) #return
for x in range(2,10,3): #for loop range function start 2, end 10, increment 3
    print(x) #return 
x = 0  # variable assignment 
while(x < 5): #while loop  start    
    print(x)  # stop
    x += 1 #increment 

pizza_toppings.pop() # Composite List delete value
pizza_toppings.pop(1) # Composite List - add value

print(person) # Composite Dictionary return 
person.pop('eye_color') # Composite Dictionary remove 
print(person) # Composite Dictionary return

for topping in pizza_toppings: 
    if topping == 'Pepperoni': # Conditional if
        continue #for loop continue
    print('After 1st if statement') #
    if topping == 'Olives': # Conditional if
        break #for loop break

def print_hello_ten_times(): #function 
    for num in range(10): # range loop starts at 0 and goes to 10
        print('Hello') #return 

print_hello_ten_times() # function call

def print_hello_x_times(x): #function paramater
    for num in range(x): #range function for loop
        print('Hello') #return

print_hello_x_times(4) # function argument

def print_hello_x_or_ten_times(x = 10): #function argument
    for num in range(x): #for loop  range function
        print('Hello') #return

print_hello_x_or_ten_times() #function call to ten
print_hello_x_or_ten_times(4) #function call with argrument to 4


"""
Bonus section
"""

print(num3)
num3 = 72 
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #key error favorite team
print(pizza_toppings[7]) # IndexError: list index out of range
   print(boolean) # indentation error unexpected indent
fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'