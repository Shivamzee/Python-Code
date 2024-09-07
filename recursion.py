# Print fibonacci series for range 20
# (1)
def fibo(n):
    if n == 0:
     return 0
    elif n == 1:
     return 1
    else:
     return fibo(n-1) + fibo(n-2)

print(fibo(3))
print(fibo(4))
print(fibo(5))



# for i in range(10):
#     print(i)