# #print is a function that is used to print the output to the console. It takes a string as an argument and prints it to the console.
# print("welcome to the day 1 of the 180 days of code challenge")

# #input is a function that is used to take input from the user. It takes a string as an argument and displays it as a prompt to the user. The user can then enter a value, which is returned as a string.
# name = input("what's your name? ")
# print("heyy " + name)

# #double quotes can be used to enclose a string that contains single quotes. For example
# #to use a single quote in a string, you can enclose the string in double quotes. For example:
# print("It's a nice day today!")
# #to use a double quote in a string, you can enclose the string in single quotes. For example:
# print('She said, "Hello!"')
# #you can also use escape characters to include special characters in a string. For example, to include a single quote in a string, you can use the escape character \'. For example:
# print("I am gonna be a \"python\"developer")

# # #f strings are a way to fomat strings in python. Theu allow you to include expressions inside string literals, using curly braces {}. the expressions inside the curly braces are evaluated at runtime and then formatted using the __format__ protocol. For example:
# print(f"heyy buddy,{name} welcome to the world of python programming")

# # #strip is a method that is used to remove any leading and tralling whitespaces from a string. It takes no arguments and returns a new string with the leading and trailing whitespaces removed. For example:
# # #upper is a method that is used to convert all the characters in a string to uppercase. It takes no arguments and returns a new string with all the characters converted to uppercase. For example:
# print(f"Hello, World! {name.strip().upper()}")

# # #capitalize is a method that is used to convert the first character of a string to uppercase and the rest of the characters to lowercase. It takes no arguments and returns a new string with the first character capitalized and the rest of the characters in lowercase. For example:
# print(f"using capitalize {name.capitalize()}")

# # title is a method that is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase. It takes no arguments and returns a new string with the first character of each word capitalized and the rest of the characters in lowercase. For example:
# print(f"using title {name.title()}")

# # # #split is a method that is used to split a string into a list of substings based on a specified delimiter. It takes a string as an argument and returns a list of substrings. For example:
# first, last = name.split(".")
# print(f"using split {first}")
# age = int(input("what's your age?"))

# # # f strings can also be used to include expressions inside string literals. For example:
# name2 = f"python programming {name} is fun your age is {age}"
# print(name2)

# # # round is a built-in function that is used to round a number to a specified number of decimal places. It takes two arguments: the number to be rounded and the number of decimal places to round to. For example:
# number = 3.14759
# rounded_number = round(number, 2)
# print(f"rounded number is {rounded_number}")

# #def main is a convention in python that is used to define the main function of a program. The main function is the entry point of the program and is executed when the program is run. It is defined using the def keyword and is usually named main. For example:
# def main():
#     print("welcome to the day 1 of the 180 days of code challenge")
#     print(hello(name))#

# #def is a keyword that is used to define a function in python. A function is a block of code that performs a specific task. It takes zero or more arguments and returns a value. For example:
# def hello(to="world"):#function definition and we can also provide a default value for the argument. For example:
#     return f"hello {to}"#return is a keyword that is used to return a value from a function. It takes an expression as an argument and returns the value of the expression to the caller. For example:

# main()

# def calculate():
#     a = int(input("enter the first number: "))
#     b = int(input("enter the second number: "))
#     operation = input("enter the operation you want to perform: ")
#     if operation == "add" or operation == "+":
#         return a + b
#     elif operation == "subtract" or operation == "-":
#         return a-b
#     elif operation == "multiply" or operation == "*":
#         return a*b
#     elif operation == "divide" or operation == "/":
#         return a/b
#     else:        return "invalid operation"

# print(calculate())

# city = input("enter the name of the city you live in: ")
# del city #del is a keyword that is used to delete a variable or an object in python. It takes a variable or an object as an argument and deletes it from memory. For example:
# print(city)
animal = ["giraffe","cat","dog"]

b = 0
def animals():
    global b
    b += 1

    if "cat" in animal:
        if "dog" in animal:
            print("giraffe is the tallest animal")

    if b < 3:
        animals()


animals()