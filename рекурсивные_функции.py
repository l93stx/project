#1 без рекурсии
def f(n):
    x = 1
    for n in range(1,n+1):
        x *= n
    return x
print(f(5))

# с рекурсией
def x(n):
    if n == 1:
        return 1
    return n * x(n-1)
print(x(5))

#2

def s(num):
    x = []
    for n in num:
        print(n**2)
s([1,2,3,4,5])