
str=input("Enter the string : ")


rev=""

for i in range(len(str)-1,-1,-1):

    rev+=str[i]


revnum = rev.upper()
print(revnum)



#print(str[::-1])