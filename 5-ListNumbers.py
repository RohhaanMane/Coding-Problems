
def listChecker(lst):
    return lst[0]==lst[-1]

lst=[]
n = int(input("Number of elements : "))

for i in range(0,n):
    ele=int(input(f"Enter element {i+1} : "))
    lst.append(ele)
res = listChecker(lst)
print(res)
