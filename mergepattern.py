from practice_set_01 import pattern

def mergepattern(n):
    count = n*2
    for i in range(n+1):
        if(i==0):
            print(' '*(count-1),'*',end='')

        print(' '*(count),end='')
        print('*'*i,end='')
        print(' '*(i*2),end='')
        print('*'*i,end='')
        print('')
        count-=2

    count1 = 1
    for i in range(n-1,0,-1):
        print(' '*(count1+1),end='')
        print('*'*i,end='')
        print(' '*(i*2),end='')
        print('*'*i,end='')
        print('')
        if(i==1):
            print(' '*(count1+1),'*',end='')
        count1+=2




pattern(4)  
mergepattern(20)
x = __name__
print(x)

