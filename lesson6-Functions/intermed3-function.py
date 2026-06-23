def calc_gmean(a ,b):
    mean = (a*b)/(a+b)
    print(mean)

def who_great(a,b):
    if (a>b):
       print("Value A is greater")
    else:
        print("Value B is greater")

a = 9
b = 20

who_great(a,b)
calc_gmean( a , b)

c = 4
d = 8

who_great(c,d)
calc_gmean(c , d)