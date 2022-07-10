
def calculate(num1, num2, operator):
    if operator=="/":
        print(f"Result: {num1 / num2}")
    elif operator=="*":
        print(f"Result: {num1 * num2}")
    elif operator=="+":
        print(f"Result: {num1 + num2}")
    elif operator=="-":
        print(f"Result: {num1 - num2}")



try:
    num1 = float(input("What is your number: "))
    num2 = float(input("What is your second number: "))
    operator = input("'/' for divide\n'*' for multiply\n'+' for add\n'-' for subtract\n")
    calculate(num1, num2, operator)
except:
    raise TypeError("Invalid Input")

