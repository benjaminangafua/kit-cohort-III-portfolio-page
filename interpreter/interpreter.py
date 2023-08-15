# Get user expression
expression = input("Expression: ")

def main():
    calculate(expression)

def calculate(val):
    num1 = float((val.split(" "))[0])
    operation = (val.split(" "))[1]
    num2 = float((val.split(" "))[2])
    if operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "/":
        print(num1/num2)
    elif operation == "*":
        print(num1*num2)
    else:
        print("Invalid")
main()

