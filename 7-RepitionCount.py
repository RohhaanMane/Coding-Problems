string = input("Enter a sentence : ")
word = input("Enter the word : ")

def rCount(string, word):
    count = 0
    str_list = string.split()

    for i in str_list:
        if i == word:
            count+=1

    return count

cnt = rCount(string, word)

print(f"{word} appeared {cnt} times")
