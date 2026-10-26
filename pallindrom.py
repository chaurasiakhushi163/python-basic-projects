# pallindrome number
print('khushi uday chourasiya-13')
num=int(input('enter a number :'))
ac_num=num
rev_num=0
while(num>0):
    rem=num%10
    rev_num=rev_num*10+rem
    num=num//10

print( rev_num,'reverse number :')

if ac_num==rev_num:
    print(ac_num, 'is pallindrome')
else:
    print(ac_num,'is not pallindrome')
