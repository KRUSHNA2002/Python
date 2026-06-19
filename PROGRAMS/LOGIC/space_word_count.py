
text=input("ENTER THE STRING : ")

space_count=0
w_count=0
word=False

for ch in text:

    if ch != " ":
       
       if word == False:
           w_count+=1
           word=True

    else:                      
      word=False
      space_count+=1

print("COUNT OF SPACE : ", space_count)
print("COUNT OF WORD : ", w_count)