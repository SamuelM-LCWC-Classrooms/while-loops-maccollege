import time

def task_1():
    password = "Password123"
    guess = input("Guess the password.")
    while guess != password:
        guess = input("Password incorrect, try again!")
    else:
        print("Password cracked!")

def task_2(): # Times table
    tt = int(input("Select your number times table."))
    terms = int(input("How many terms should be outputted?"))
    repeat = 1
    while repeat <= terms:
        output = tt*repeat
        print(output)
        repeat = repeat + 1
    # Enter your code here

def task_3():
     # Count mississippis
     count = 1
     while count != 6:
         print(count, "Mississippis")
         count = count + 1
         time.sleep(1)
print(task_3())