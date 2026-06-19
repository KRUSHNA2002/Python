#  Task 1 — Number Analyzer (Beginner Logic)

num=int(input("ENTER THE NUMBER : "))

if num >0:
    print("Number is positive")
elif num==0:
    print("Number is 0")
else:
    print("Number is negative")

if num % 2==0:
    print("Number is even")

else:
    print("Number is odd")
    
if num % 3 ==0 and num%5==0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is Not divisible by 3 and 5")
        



