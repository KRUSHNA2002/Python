
list1=[1,4,7,9,33,40,55,55]

largenum=0

seclargenum=0

thirdlarge=0

for i in list1:

   if i > largenum:

     seclargenum=largenum
     largenum=i
   
   if seclargenum > i and seclargenum !=largenum:
      
      seclargenum=i

print(largenum)
print(seclargenum)
