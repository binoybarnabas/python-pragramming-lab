test_string = input("enter the string")
all_freq = {}
for i in test_string:
  if i in all_freq:
    all_freq[i]+=1
  else:
    all_freq[i]=1
print("count of all characters in",test_string,"is:",str(all_freq))
