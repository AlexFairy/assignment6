# 1. The Calculator App-------------------------------------------------------------------------------
# Objective: 
# The aim of this assignment is to build a basic calculator that can perform 
# addition, subtraction, multiplication, and division.

# Task 1: 
# Create functions for each arithmetic operation.

#Task 2: 
# Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

# Task 3: 
# Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def add(x, y):
  return x + y

def minus(x, y):
  return x - y

def times(x, y):
  return x * y

def divide(x, y):
  if x == 0 or y == 0:
    print('You cannot divide by Zero')
  else:
    return x / y

x = int(input("Enter number: "))
operator = int(input("Type 1 for addition\nType 2 for subtraction\nType 3 for Multiplication\nType 4 Division: "))
y = int(input("Enter number: "))

if operator == 1:
  print(f"{x} + {y} = {add(x, y)}")
elif operator == 2:
  print(f"{x} - {y} = {minus(x, y)}")
elif operator == 3:
  print(f"{x} * {y} = {times(x, y)}")
elif operator == 4:
  print(f"{x} / {y} = {divide(x, y)}")

# 2. The Shopping List Maker----------------------------------------------------------------------------
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.

#Task 2: Include a function to remove items from the list.

#Task 3: Add a function that prints out the entire list in a formatted way.

item_list = []

def add_item(item):
  global item_list
  item_list.append(item)

def remove_item(item):
  global item_list
  item_list.remove(item)

def display_list():
  global item_list
  for i in range(len(item_list)):
    print(f"Item: {item_list[i]}")

  while True:
    action = input("Choose an action: [A]dd item, [R]emove item, [D]isplay item's list, [Q]uit: ")
    if action.lower() == 'a':
      item = input("Enter the item name: ")
      add_item(item)
    elif action.lower() == "r":
      item = input("Which item to remove from list: ")
      remove_item(item)
    elif action.lower() == "d":
      display_list()
    elif action.lower() == "q":
      break
    else:
      print("Invalid action. Please choose again")

add_item(iter), remove_item(iter), display_list()

#Note: 
# The goal of this is to be a program. 
# The recommendation is to use a while loop that will allow the user to 
# continue to add, remove, and print off their shopping list until they 
# decide to "quit", also known as breaking the loop.
