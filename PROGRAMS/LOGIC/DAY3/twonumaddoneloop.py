
list1 = [1,5,8,3,6,2,8,1]

target=9

store={}

for i in range(len(list1)):

    need=target-list1[i]

    if need in store:
        print(store[need], i)
        break

    store[list1[i]] = i