
dist=[1,4,8,9,-10,3,2,6,3]

# Example 1
# def findmax(maxnum):
      
#       return max(maxnum)

# print(findmax(dist))


# Example 2

maxnum=dist[0]

for i in dist:

    if i > maxnum :

        maxnum=i

print(maxnum)