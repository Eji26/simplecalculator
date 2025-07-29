# Basic Calculator Program

def main():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please use +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
