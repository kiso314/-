def Congruence_judgment(a,b,n):
    if((a-b)%n==0):
        return True
    else:
        return False

a=int(input("请输入第一个整数:"))
b=int(input("请输入第二个整数:"))
n=int(input("请输入模n:"))

if(Congruence_judgment(a,b,n)):
    print("{}与{}模{}同余".format(a,b,n))
else:
    print("{}与{}模{}不同余".format(a,b,n))

