print("Welcome to the calculator program")
print("---------------------------------")
counter = 0

while True:
    
    user_input = input("Enter 1 for calculator mode; 2 for counter mode; Enter 'exit' for exit : ")
    print("---------------------------------")
    
    if user_input == "1":
     
        print("Calculator mode")
        print("----------------")
        
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        print("----------------")
    
        if operator == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        
        elif operator == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        
        elif operator == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        
        elif operator == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        
        elif operator == "//":
            print(f"{num1} // {num2} = {num1 // num2}")
        
        elif operator == "**":
            print(f"{num1} ** {num2} = {num1 ** num2}")
        
        elif operator == "%":
            print(f"{num1} % {num2} = {num1 % num2}")
        
        else:
            print("Invalid operator")
        
        print("----------------")

    elif user_input == "2":
        
        print("Counter mode; Use '+' for increment and '-' for decrement")
        print("----------------")
        count = int(input("Enter counter value: "))
        
        if count == '+':
            counter += 1
            print(f"Counter value: {counter}")
        
        elif count == '-':
            counter -= 1
            print(f"Counter value: {counter}")
        
        else:
            print("Invalid input")
    
    elif user_input == "exit" :
        break
    
    else:
        print("Invalid input")