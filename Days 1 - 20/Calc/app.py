def calculation():
    a = int(input("Type the first number?\n"))
    argv = str(input(("+ - * /\n")))
    b = int(input("Type the second number?\n"))
    if argv == "+":
        return a + b
    elif argv == "-":
        return a - b
    elif argv == "*":
        return a * b
    elif argv == "/":
        return a / b
    else:
        print("Wrong input!")
        return
state = True
while state:
    print("Result: ", int(calculation()))
    choice = str(input(("\nPrint 'y' to exit calculation. Print 'c' to continue calculation\n"))).lower()[0]
    if choice == 'y':
        state = False
    elif choice == 'c':
        continue
    else:
        print("Wrong option")

     