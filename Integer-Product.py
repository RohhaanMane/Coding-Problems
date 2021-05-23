'''
Q1 - Accept two integer numbers from a user and calculate their product.
     if th product is greater than 1000 return their sum as Result
     else return their product as Result
'''


num1 = int(input('Enter First Number : '))
num2 = int(input('Enter Second Number : '))

def calculate(num1,num2):
    prod = num1 * num2

    if prod > 1000:
        return num1+num2
    else:
        return prod

result = calculate(num1,num2)
print('Result : ',result)
