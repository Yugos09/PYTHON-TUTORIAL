def main():
    try:
        num1 = int(input('Type the first number '))
        num2 = int(input('Type the second number '))
    except ValueError:
        return "Please enter a valid number."

    return(division(num1, num2))

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You cannot divide by zero"

print (main())