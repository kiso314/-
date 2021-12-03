
#扩展欧几里得算法的函数
def ext_euclid(a, b):     
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = ext_euclid(b, a % b)         
        x, y = y, (x - (a // b) * y)         
        return x, y, q

#运用扩展欧几里得算法求模逆元
def get_inversr(a,b):
    return ext_euclid(a,b)[0]

#中国剩余定理
def CRT(b_list,m_list):
    M=1
    for mi in m_list:
        M=M*mi
    #计算Mi
    Mi_list=[]
    for mi in m_list:
        Mi_list.append(M//mi)
    #计算Mi的模逆元
    Mi_inverse=[]
    for i in range(len(Mi_list)):
        Mi_inverse.append(get_inversr(Mi_list[i],m_list[i]))
    #计算解x
    x=0
    for i in range(len(b_list)):
        x+=Mi_list[i]*Mi_inverse[i]*b_list[i]
        x%=M
    return x

#判断列表中元素是否两两互素
def ifcoprime(ls):
  for i in range(len(ls)):
    for j in range(i+1,len(ls)):
      if ext_euclid(ls[i],ls[j])[2]!=1:
        return 0  


#输入bi,mi
while True:
    m_list=[]
    b_list=[]
    
    b_i=input("请输入bi，以空格分隔:")
    b_i=b_i.split( )
    for i in b_i:
      b_list.append(int(i))
    
    m_i=input("请输入mi，以空格分隔:")
    m_i=m_i.split( )
    for i in m_i:
      m_list.append(int(i))
    
    if len(m_list)!=len(b_list):
      print("mi的个数和bi的个数不相同，请重新输入\n")
    elif ifcoprime(m_list)==0:
      print("输入的mi并不是两两互质的，请重新输入mi\n")
    else:
      break

x=CRT(b_list,m_list)
print("同余式方程组的解为{}".format(x))