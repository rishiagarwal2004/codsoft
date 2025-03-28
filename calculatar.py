def calculator():
    while True:
        print("\nSimple Calculator")
        print("1 for Addition")
        print("2 for Subtraction")
        print("3 for Multiplication")
        print("4 for Division")

        perform = input("Enter what you want to perform: ")

        if perform in ('1', '2', '3', '4'):
            num1 = float(input("Enter num1: "))
            num2 = float(input("Enter num2: "))

            if perform == '1':
                print(f"{num1} + {num2} = {num1 + num2}")  
            elif perform == '2':
                print(f"{num1} - {num2} = {num1 - num2}")                                
            elif perform == '3':
                print(f"{num1} * {num2} = {num1 * num2}")               
            else:
                if num2 == 0:
                    print("Invalid number: Division by zero is not allowed")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")  
        else:
            print("Task not performed by calculator")
        
        # Ask the user if they want to perform another calculation
        again = input("\nDo you want to perform another calculation? (Yes/No): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator.")
            break

calculator()
