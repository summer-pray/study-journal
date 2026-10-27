def first(n):
    x=0
    try:
        x=second(n)
    except:
        x+=1
    return x
def second(n):
    y=2
    try:
        y=third(n)
    except:
        y/=2*n
    return y
def thrid(n):
    return 1/n/(n-1)




    