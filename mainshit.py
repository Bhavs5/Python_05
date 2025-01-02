# IF STATEMENTS

# age = int (input("Enter your age: "))

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a child")        

# response = input("Would u like food? (yes/no) ")

# if response == "yes":
#     print("Have some food")
# else:
#     print("Ok, no food for you")   

# name = input("Enter your name: ")

# if name == "":
#     print("Complete the field")
# else:
#     print(f"Hello, {name}")   

# for_sale = False 

# if for_sale:
#     print("The item is for sale")
# else:
#     print("The item is not for sale") 


# LOGICAL OPERATORS
            #evaluates multiple conditions
            #OR = at least one condition is true
            #AND = all conditions are true
            #NOT = inverts the condition (not False = True, not True = False)


# temp = 30
# is_raining = False 
# is_sunny = True

# if temp < 20 or temp < 0 or is_raining:
#     print("Stay inside")
# else:
#     print("Go outside")

# if temp >= 29 and is_sunny:
#     print("It's hot outside")
#     print("Stay hydrated")
# elif temp <= 0 and is_sunny:
#     print("It's cold outside")
#     print("And sunny too")
# else:
#     print("It's ok outside")

# if temp >= 29 and not is_sunny:
#     print("It's hot outside")
#     print("Stay hydrated")
# elif temp <= 0 and  not is_sunny:
#     print("It's cold outside")
#     print("And sunny too")
# else:
#     print("It's ok outside 🌞 🍃")


# CONDITIONAL EXPRESSIONS 
#       i.e one liner for if-else statements(TERNARY OPERATORS)

#formula->  X if condition else Y

# num = 10

# print("Positive" if num > 5 else "Negative")

# num = 15
# result = "even" if num % 2 == 0 else "odd"
# print(result)

# num = 0
# a = 10
# b = 20
# result = "+" if num > 0 else "-" if num < 0 else "0"
# more than 2 conditions can be put at once.
# max_num = a if a > b else b
# print(max_num)


# STRINGS

# name = "John"
name = input("Enter your name: ")

# result = len(name)+ len(name1)  #includes spaces too.
result  = name.find("B")
print(result)