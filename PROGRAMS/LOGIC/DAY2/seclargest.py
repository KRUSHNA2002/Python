
list1=[7,2,5,6,3,90]

largestnum=0
seclargest=0

for num in list1:

    if num > largestnum:
        seclargest=largestnum
        largestnum=num

    if num > seclargest and num != largestnum:
        seclargest=num


print(largestnum)
print(seclargest)
