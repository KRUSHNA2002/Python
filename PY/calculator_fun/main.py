import add
import sub
import mul
import div
num1=int(input("Enter first num1..."))
num2=int(input("Enter first num2..."))

ope=input("Enter CHoice:" \
" Enter 1 for (+), " \
"2 for (-), " \
"3 for (*), " \
"4 for (/)")

match ope:

    case "1":
        print(add.add(num1,num2))
    case "2":
        print(sub.sub(num1,num2))
    case "3":
        print(mul.mul(num1,num2))
    case "3":
        print(div.div(num1,num2))
    case _:
       
          print("exit")