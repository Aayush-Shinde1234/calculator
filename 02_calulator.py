# Calculator
print("="*30)
print("     SMART CALCULATOR")
print("="*30)
user = "yes"
while user.lower() == "yes" :
    num1 = float(input("Enter a number :"))
    num2 = float(input("Enter a number :"))

    operation = input("Enter operation (+,-,*,/,**) :").strip().lower()
    if(operation == "*") :
        print(f"Result :{num1*num2}")
    elif(operation == "+") :
        print(f"Result :{num1+num2}")
    elif(operation == "-") :
        print(f"Result :{num1-num2}")
    elif(operation == "**") :
        print(f"Result : {num1**num2}")
    elif(operation == "/") :
        if (num2 !=0):   
            print(f"Result : {num1/num2}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")
    
    user = input("\nDo you want to continue  yes/no :")
print("="*30)

