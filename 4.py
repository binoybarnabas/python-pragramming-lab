#Count the occurrences of each word in a line of text.

textline = input("enter the line of text")

textlist = textline.split(" ")

newlist = {x:textlist.count(x) for x in textlist}
print(newlist)
