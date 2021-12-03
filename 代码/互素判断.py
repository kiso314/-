def division_algorithm(m,n):
    while(n%m!=0):
        m,n=n%m,m
    return m

def Relatively_prime(a,b):
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
    if(gcd==1):
        return True
    else: return False

a=int(input("请输入第一个整数:"))
b=int(input("请输入第二个整数:"))

if(Relatively_prime(a,b)):
    print("{}和{}互素".format(a,b))
else: 
    print("{}和{}不互素".format(a,b))
