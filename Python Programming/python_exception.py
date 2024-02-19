def quotient (a,b):
    return a / b

try:
    print(quotient(5,0))
#Specific exception
except ZeroDivisionError as e:
    print(e,': we cannot divide by zero')
#Generic exeption
except Exception as e:
    print('something went wrong:',e)
    print(e.__class__)

