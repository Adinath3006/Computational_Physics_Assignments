""" Exercise 7 """

""" We generate the catalan numbers recursively """

def Catalan_Num(i):
    if i == 0:
        return 1
    else:
        Catalan = 1
        for j in range(0,i+1):
            Catalan *= (4*j+2)/(j+2)
        return Catalan

i = 0
while Catalan_Num(i) <= 10**9:
    print(Catalan_Num(i))
    i = i+1
    
""" The Catalan numbers less than or equal to one billion are:
    1
    1.0
    2.0
    5.0
    14.0
    42.0
    132.0
    429.0
    1430.0
    4862.0
    16796.0
    58786.0
    208012.0
    742900.0
    2674440.0
    9694845.0
    35357670.0
    129644790.0
    477638700.0"""