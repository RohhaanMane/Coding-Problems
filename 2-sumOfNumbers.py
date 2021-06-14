'''
Given a range of first 10 numbers, Iterate from start number to the end number and print sum of current number and privious number
'''


def sumNum(num):
    prevNum = 0

    for i in range(num):
        sum = prevNum+i
        print("Current:",i, "Privious:",prevNum, "Sum: ",sum)
        prevNum=i

num = int(input("Enter a number: "))
sumNum(num)
