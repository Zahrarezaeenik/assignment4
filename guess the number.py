import random
pc_number=random.randint(0,20)
counter=0
while True:
    user_number=int(input("Enter your number: "))
    counter+=1
    if user_number==pc_number:
        print("brande shodi!!!")
        break
    elif user_number<pc_number:
        print("boro balatar!")
    else:
        print("boro paientar!")

print(f"The number of your guesses is {counter}")