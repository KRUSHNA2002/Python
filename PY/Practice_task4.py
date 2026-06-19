num1=input("Enter Num1...")
num2=input("Enter Num2...")

num1=int(num1)
num2=int(num2)
operator=input("Enter operator")

match operator:
    case "+":
        print(num1 + num2)
    case "-":
         print(num1 - num2)
    case "*":
         print(num1 * num2)

    case "/":
          print(num1 / num2)
    case _:
          print("Invalid Error")