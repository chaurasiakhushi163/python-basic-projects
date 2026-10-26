num=int(input(' enter a number : '))
if num==0 or num==1:
    print('the entered no is not a prime number',num)
for i in range(2,num):
    if num%i==0:
        flag=0
        break
    else:
        flag=1
        break
if flag==0:
    print('is not a prime number')
else:
    print('is a prime number')
