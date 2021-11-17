string = input("enter the sentence")
print(string)
newsplit = string.split(" ")
print(newsplit)
length = len(newsplit)
count = 0
counter = [0]*10
for i in range(0,length,1):
    newsplit1 = newsplit[i]
    for j in  range(0,length,1):
        if(newsplit1 == newsplit[i]):
            count = count+1
        counter[i] = count
    count = 0
for i in range(0,length,1):
    print(newsplit[i],"number of occurences is",counter[i])

#print("number of words in the string is",length)
