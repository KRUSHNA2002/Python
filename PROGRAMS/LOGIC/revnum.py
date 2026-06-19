
num=int(input("ENTER THE NUM "))

revnum=0

while(num > 0):

    digit= num % 10
    revnum = revnum * 10 + digit            #       PROGRAM FOR REVERSE NUM
    # revnum =  digit * digit * digit       #       PROGRAM FOR CUBE OF  NUM
    num= num // 10
    


print(revnum)


revnum =  digit * digit * digit