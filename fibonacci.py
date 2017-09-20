n1 = 0
n2 = 1
print (n1,end=',')
print (n2,end=',')

for n3 in range (0,100):
    n3 = n2+n1
    print (n3,end=',')
    n1 = n2
    n2 = n3
