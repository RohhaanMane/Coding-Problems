
def evenIndex(string):
    for i in range(0,len(string),2):
        print("index[",i,"]", string[i])

string = input('Enter a string: ')
evenIndex(string)
