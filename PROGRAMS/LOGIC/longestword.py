text=input("ENTER THE STRING : ")

current=0
w_count=0
current_word=""
name=""
char=True

for ch in text:
    if ch != " ":
       
        current+=1

        current_word+=ch

    elif ch==" ":
        if current > w_count:
            w_count = current
            name = current_word
        current=0
        current_word=""

if current > w_count:
        w_count = current
        name = current_word


print("Longest word count is : ", w_count)
print("Longest name is : ", name)
    
