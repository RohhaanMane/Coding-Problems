
num = [10,20,33,46,55]
divN = int(input("Enter Divisor: "))

def divByNum(num):
    for i in num:
        if i%divN==0:
            print(i)

print(divByNum(num))
