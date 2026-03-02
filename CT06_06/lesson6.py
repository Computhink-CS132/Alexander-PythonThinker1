print("Hello from lesson 6")

# Lesson 6 - Debugging

## Recap 1: Class Average Calculator

# sum = 0

# ttl = int(input("What is the total number of students?"))

# for i in range(ttl):

#     mark = int(input("What is the marks of this student?"))

#     sum += mark

# print(sum)

# average = sum / ttl

# print("Class average = " + str(average))

## Task 1: Syntax Errors

# Fix the errors in the following:

# **Task 1a**

# for i in range(3):

#     print("Hello, World!")

# **Task 1b**

# for i in range(5):

#     print(i)

# **Task 1c**

# print("Hello, World!")

# **Task 1d**

# I = 5

# **Task 1e**

# print ("Hello, World!")

## Task 2: Name Errors

# Fix the errors in the following:

# **Task 2a**

# print("age")

# **Task 2b**

# name = ("Alice")

# print(name)

# **Task 2c**

# x = 5

# print(x)

# **Task 2d*

# print("Hello, World!")

## Task 3: Type Errors

# Fix the errors in the following:

# **Task 3a**

# age = ("25")

# print(age + "1")

# **Task 3b**

# number = 10

# print(number - 5)


# **Task 3c**

# print("Repeat" + "3")

# **Task 3d**

# year = 2023

# print("The year is " + str(year)

# **Task 3e**

x = 10

y = x / 2

# **Task 3f**

# end = 5

# for i in range(end):

#     print(i)


# ############### Revision Practice ###############

# ### Ask the pizza man how much the pizza costs?

# price = int(input("How much does one pizza cost."))

# ### How many students are there?

# num = int(input("How many students are there?"))

# ### Find out how much each student should pay for their slice?

# print("Each student should pay " + ("$") , round(price / num) , ("."))

# ############### Revision Practice 2 ################## 

### 1. Ask the user how many steps did you take each day
total_steps = 0
steps = int(input("How many steps did you take each day?"))

###2. Ask the user how many days do you want to walk?
num_of_days = int(input("How many days do you want to walk?"))

# 3. Add each day you take the num of steps

for i in range(num_of_days):

    total_steps += steps

### 4. print the total num of steps taken:

print("Day" , " Number of steps: " , total_steps)