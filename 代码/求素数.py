from time import *
def sieve_func(n):
    prime=[]
    sieve = [True] * (n+1)
    for i in range(2, n):
        if sieve[i]:
            prime.append(i)
            for j in range(i * i, n, i):
                sieve[j] = False
    return prime

n=input("请输入素数的范围n：")
begin_time=time()
sieve_func(int(n))
end_time=time()
run_time=end_time-begin_time
print('运行时间：{}'.format(run_time))