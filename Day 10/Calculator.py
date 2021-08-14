import art
import os
def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": division
}

def calculator():
  print(art.logo)

  num1 = float(input("Enter the first number : "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operator = input("Pick an operation: ")
    num2 = float(input("Enter the next number : "))
    calculation_function = operations[operator]
    value = calculation_function(num1, num2)

    print(f"{num1} {operator} {num2} = {value}")

    user = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation or type 'e' to exit: ")
    if user == 'y':
      num1 = value
    elif user == 'n':
      should_continue = False
      os.system('cls')
      calculator()
    elif user == 'e':
        return
    else:
        print("Invalid selection !!")
calculator()