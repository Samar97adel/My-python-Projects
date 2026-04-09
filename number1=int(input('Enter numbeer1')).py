num1=float(input('enter first number: '))
operator=input('Enter operator (+,_,*,/)')
num2=float(input('Enter second number: '))
if operator == "+":
    result=num1+num2
    print('num1+num2= ', result)
elif operator=="-":
    result=num1-num2
    print('num1-num2= ',result)
elif operator=='*':
    result=num1*num2
    print('num1*num2= ', result)
elif operator=='/':
     if num2 != 0:
         result = num1/num2
         print('num1/num2',result)
     else:
         print('Error: Division by zero is not allowed')
else:
    print('invalid operator! Please use +,-,* or /')
    
