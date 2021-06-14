
'''
Accept string from a user and display only those characters which are present at even index number
'''

def indexNum(string):
    for i,c in enumerate(string):
        if(i%2==0):
            print(c)


string = input("Enter a string: ")
indexNum(string)
