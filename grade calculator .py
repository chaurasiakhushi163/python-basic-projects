# grade calculator 
pnum=float(input('physics marks:'))
mnum=float(input('maths marks:'))
cnum=float(input('chemistry marks:'))
Enum=float(input('Enum marks:'))
tmarks=pnum+mnum+cnum+Enum
print('total marks=',tmarks)
print('average marks:',tmarks/4)
percent=((tmarks/400)*100)
print('percentage:',percent)
if percent>=80:
    print('Congratulationss u got O grade')
elif percent>=70:
     print('Congratulations u got A grade')
elif percent>=60:
     print(' congratulations U got B grade')
elif percent>=50:
     print('U got C grade')
elif percent>=40:
     print('U got D grade')
else:
    print('u failed')





         



     

