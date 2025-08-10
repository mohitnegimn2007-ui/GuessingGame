import random




for i in range(1,11):
    computer=random.randint(1,100)
    print("Attempt:",i)
    you=int(input("Enter your guess:"))
    print("Computer guess is:",computer)
    if(you>computer):
        print("Lower number please")
    elif(you<computer):
        print("Higher number please")

    elif(you==computer):
        print("Wow!Its a Perfect guess")
        break
    if(i==10):
        print("Out of attempts")
