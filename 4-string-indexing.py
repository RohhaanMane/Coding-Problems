

# def removeChars(string, num):
#     if len(string)>num:
#         return string.replace(string[:num],"")
#     else:
#         return "Enter smaller number than length of string"
def remChar(string, num):
    return string[num:]

s = input("Enter string : ")
n = int(input("Enter Number : "))

res = remChar(s,n)
print(res)
