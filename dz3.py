import random
i = 0
b = 0
a = random.randint(1, 1000)


while True:
    b = int(input("Choose door: "))
    if(a == b):
        print("Correct")
        break
    else:
        print("No")
    i += 1
    if (i == 10):
        print("Sorry")
        break
