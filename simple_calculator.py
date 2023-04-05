# Simple Calculator
num1 = float(input("Input 1st number: "))
num2 = float(input("Input 2nd number: "))

def add(num1, num2):
    ans = num1 + num2
    return ans 


def sub(num1, num2):
    ans = num1 - num2
    return ans


def add(num1, num2):
    ans = num1 + num2
    return ans


def mul(num1, num2):
    ans = num1 * num2
    return ans


def div(num1, num2):
    ans = num1 / num2
    return ans


Operation = str(input(
    "What operation do you want to carry out?:\n('add'- addition)\n('sub'- subtraction)\n('mul'-multiplication)\n('div'-division)"
))
if (Operation == "add"):
        print(add(num1, num2))
elif (Operation == "sub"):
        print(sub(num1, num2))
elif (Operation == "mul"):
        print(mul(num1, num2))
elif (Operation == "div"):
        print(div(num1, num2))
else:
        print("Error not a valid operation.")
        