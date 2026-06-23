
# def fibo(n):
#     a,b=0,1
#     for _ in range(n):

#         print(a,end=" ")
#         a,b = b,a+b
# fibo(10)



def fibo(n):

    if n<=1:
        return n
    
    return fibo(n-1) + fibo(n-2)


for i in range(11):
    print(fibo(i), end=" ")