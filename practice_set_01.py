def space(n):
    print(" "*n,end='')
    # for i in range(n):

def star(p):
    # for i in range(p):
    print('*'*p,end='')


# class printpattern():
def pattern(b):

    # start of right side
    for i in range(b+1):
        space(i)
        star(i)
        print('')

        # reverse of right side
    for i in range(b+1,0,-1):
        space(i)
        star(i)
        print('')



   





        



