print("Enter an operator(+,_,*,/,^)")
choice=input("your choice:")
if choice in('+','_','*','/'):
    num1=float(input("1st number:"))
    num2=float(input("2nd number:"))
    if choice=='+':
        print(num1+num2)
    elif choice=='_':
        print(num1_num2)
    elif choice=='*':
        print(num1*num2)
    elif choice=='/':
        print(num1/num2)
    elif choice=='^':
        print(num1^num2)
    else:
        print("Invalid Input")