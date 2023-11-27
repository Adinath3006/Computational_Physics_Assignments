""" Exercise 10 """

# Part A

def binomial(n,k):
    if n < k:
        print("Invalid input!")
    else:
        if k == 0:
            return 1
        elif k >= 1:
            n_k = n
            for i in range(2,k+1):
                n_k *= (n-i+1)/i
            return int(n_k)
        else:
            print("Invlaid input!")

# Part B

for n in range(1,21):
    for k in range(0,n+1):
        print(binomial(n,k), end=" ")
    print('\n')

"""The first 20 lines of the pascal triangle is
1 1 

1 2 1

1 3 3 1

1 4 6 4 1

1 5 10 10 5 1

1 6 15 20 15 6 1

1 7 21 35 35 21 7 1

1 8 28 56 70 56 28 8 1

1 9 36 84 126 126 84 36 9 1

1 10 45 120 210 252 210 120 45 10 1 

1 11 55 165 330 461 461 329 164 54 10 0

1 12 66 220 495 792 924 792 495 220 66 12 1

1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1

1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1

1 15 105 454 1364 3002 5004 6434 6434 5004 3002 1364 454 104 14 0

1 16 120 560 1820 4368 8008 11440 12870 11440 8007 4367 1819 560 120 16 1

1 17 136 680 2380 6188 12376 19448 24310 24310 19448 12376 6188 2380 680 136 17 1

1 18 153 816 3060 8568 18564 31824 43758 48620 43758 31824 18564 8568 3060 816 153 18 1

1 19 171 969 3876 11628 27132 50388 75582 92378 92378 75582 50388 27132 11628 3876 969 171 19 1 

1 20 190 1140 4845 15504 38760 77520 125970 167960 184756 167960 125970 77520 38760 15504 4845 1140 190 20 1"""

# Part C

# (a)
print("The probability that an unbiased coin, tossed 100 times, will come up heads exactly 60 times is {:.7f}".format(binomial(100,60)/2**(100)))

"""The probability that an unbiased coin, tossed 100 times, will come up heads exactly 60 times is 0.0108439"""

sum = 0
for i in range(60,101):
    sum += binomial(100,i)

# (b)
print("The probability that it comes up heads 60 or more times is {:.7f}".format(sum/2**(100)))

"""The probability that it comes up heads 60 or more times is 0.0284440"""