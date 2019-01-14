#to print pattern
#pattern 1
n=int(input('Enter number of rows to print:')) #by default it is character type
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ') #by default end='\n'
    print()

#pattern 2
n=int(input('Enter number of rows to print:'))
for i in range(1,n+1):
    for j in range(1,n+i):
        if j<=(n-i):
            print(' ',end=' ')
        else:
            print('*',end=' ') #by default end='\n'
    print()



#pattern 3
n=int(input('Enter number of rows to print:'))

for i in range(1,n+1):
    flag=1
    for j in range(1,n+i):
        if j<=(n-i):
            print(' ',end=' ')
        elif flag==1:
            print('*',end=' ') #by default end='\n'
            flag=0
        elif flag==0:
            print(' ',end=' ')
            flag=1
    
    print()


#pattern 4
n=int(input('Enter number of rows to print:'))
for i in range(1,n+1):
    k=0
    for j in range(1,2*i):
        if j>i:
            k=k-1
            print(k,end=' ')
        else:
            k=k+1
            print(k,end=' ') #by default end='\n'
            
    print()

#pattern 5
n=int(input('Enter number of rows to print:'))
for i in range(1,n+1):
    k=0
    for j in range(1,n+i):
        if j<=(n-i):
            print(' ',end=' ')
        elif  j>n:
            k=k-1
            print(k,end=' ')
        else:
            k=k+1
            print(k,end=' ') #by default end='\n'
    print()














