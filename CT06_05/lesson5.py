print("Hello from lesson 5")

## Recap 1: Automated Birthday Invitation

# name = input("What is this person's name?")

# age = input("What is their age?")

# message = input("What is the message you want to send them?")

# print(("Happy ") + age + ("th birthday ") + name + ("!")  + ("here is a message ") + message

## Task 1: Repeated Sentence Loop

# for count in range (100):

#     print("I like chicken rice.")

## Task 2: Sentence Repetition Loop with Order of Code
##         Sequence

# for count in range (100):

#     print("I like cake,")

#     print("give me more!")

# Task 3: range(stop)#

# for number in range(0,59):

#     print(number)

## Task 4: range(start, stop)

# **Task 4a**

# for count in range(1,6):

#     print(count)

# **Task 4b**

# for count in range(51,101):

#     print(count)

# **Task 4c**

# for count in range(18,30):

#     print(count)

## Task 5: range(start, stop, step)

# **Task 5a**

# for count in range(2,25,2):

#     print(count)

# **Task 5b**

# for count in range(8,97,8):

#     print(count)

# **Task 5c**

# for count in range(5,0,-1):

#     print(count)

## Task 6: Countdown timer

# **Task 6a**

# print("Ready!")

# for count in range(3,0,-1):

#     print(count)

# **Task 6b**

# for count in range(10,0,-1):

#     print(count)

# print("Boo!")

## Task 7: User-Defined Range Counter

# start = int(input("Ven do you vant to start?"))

# stop = int(input("Ven do you vant to stop?"))
# if stop > start:

#     for count in range (start,stop + 1):
#         print(count)

# else:

#     for count in range (start,stop - 1, -1):
        
#         print(count)

## Task 8: Accumulative Sum in Loop

# num = 0

# for count in range(0,9):

#     num = num + count

#     print(num)

## Task 9: Name Cheer

name = input("What is your name?")

for char in name:

    print("Give me a " + char + "!")

print("What do we have?")

print(name + " is the best!")

