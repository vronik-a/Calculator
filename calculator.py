x = int(input('Enter first number '))
operator = input('choose operator ')
y = int(input('Enter second number '))

if (operator == '+'):
    print(x+y)
elif (operator == '-'):
    print(x-y)
elif (operator == '*'):
    print(x*y)
elif (operator == '/'):
    print(x/y)
elif (operator == '%'):
    print(x%y)
elif (operator!='+' or operator !='-' or operator !='*' or operator !='/'):
    print("the operator isn't correct")
    operator = input('choose between +, -, *, /, or % ')
    if (operator == '+'):
        print(x+y)
    elif (operator == '-'):
        print(x-y)
    elif (operator == '*'):
        print(x*y)
    elif (operator == '/'):
        print(x/y)
    elif (operator == '%'):
        print(x%y)