
list1 = [4,5,8,3,6,2,8,1]

target=9
flag=True

nums=[]

for i in range(len(list1)):

    for j in range(i+1,len(list1)):

        if list1[i] + list1[j] == target:
           
           if flag==True:

            print("Numbers is addi {addi} is : ",list1[i],"and ",list1[j])

            flag=False

            nums.append(list1[i])
            nums.append(list1[j])
                

print(nums)