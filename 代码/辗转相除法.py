'''
def division_algorithm(m,n):
    while m*n!=0:
        m=m%n
        if(m==0):
            return n
        else:
            n=n%m
            if(n==0):
                return m
'''
def division_algorithm(m,n):
    while(n%m!=0):
        m,n=n%m,m
    return m

a=int(input("请输入第一个整数:"))
b=int(input("请输入第二个整数:"))
gcd=0
if(a<0):
    a=-a
if(b<0):
    b=-b
if(a==0 and b==0):
    gcd=0
elif(a==0 or b==0):
    gcd=a+b
else:
    gcd=division_algorithm(a,b)
print("最大公因子为：")
print(gcd)

