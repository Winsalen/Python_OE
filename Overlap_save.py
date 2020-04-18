import numpy as np

print ('N point DFT value')
N=int(input())

lst1 = []
n1=int(input('Enter the no. of elements in x(n): '))
print ('Enter the elements in x(n)')
for i in range(0,n1):
    x=int(input())
    lst1.append(x)
print ('x(n) :', lst1)

lst2 = []
n2=int(input('Enter the no. of elements in h(n): '))
print ('Enter the elements in h(n)')
for j in range(0,n2):
    h=int(input())
    lst2.append(h)
print ('h(n) :', lst2)

l=n1+n2-1
M=len(lst2)
L=N-M+1
#print('L :', L)
h1 = []
for k in range (0,L-1):
    lst2.append(0)
    h1=lst2    
#print("h'(n) :", h1)
H1=np.fft.fft(h1,N)
#print ("FFT of h'(n) :", H1)

num=0
Q=len(lst1)//L
R=len(lst1)%L
if R!=0:
    for i in range (L-R):
        lst1.append(0)
        num=Q+1
else:
    num=Q
while num*L<l:
    lst1.append(0)
    num+=1

lst3 = []
for i in range (0,M-1):
    lst3.append(0)
lst = []
split = []
lst4 = []
for i in range (0,len(lst1),L):
    z=i
    split = lst1[z:z+L]
    lst = lst3+split
    length=len(lst)
    if length!=N:
        for j in range (0,N-length):
            lst.append(0)
    lst4.append(lst)
    lst3 = lst[N-(M-1):N]
#print (lst4)

res=[]
for i in range (0,len(lst4)):
    lst5 = []
    F=[]
    y=[]
    F=np.fft.fft(lst4[i],N)
    for j in range (0,len(H1)):
        lst5.append(F[j]*H1[j])
    y=np.fft.ifft(lst5)
    res.append(y)

ans=[]
for i in range (0,len(res)):
    ans.append(res[i][M-1:len(res[i])])

Result=[]
for i in ans:
    Result.extend(i)

for i in range (len(Result)-1,1,-1):
    if Result[i]<=0.1:
        Result.remove(Result[i])
    else:
        break
print ("The Result is :", Result)