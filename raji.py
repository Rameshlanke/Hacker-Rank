# x = int(input())
# a = int((x-1)/3)
# b = int((x-1)/5)
# p = a*(6 + (a-1)*3)/2
# q = b*(10 + (b-1)*5)/2
# r = p+q
# print (r)


# a = 0
# d = 0.5
# n = 8
# ap = np.arange(a, a + n*d, d).tolist()


import numpy as np
for i in range(int(input())) :
    x = int(input())
a = 3
d = 3
n = int((x-1)/3)
t3 = np.arange(a, a + n*d, d).tolist()

p = 5
q = 5
r = int((x-1)/5)
t5 = np.arange(p, p + r*q, q).tolist()

final = set(t3 + t5)
print(sum(final))





def calculate_sum_of_multiples(n):
    sum_of_multiples = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples

t = int(input())

for i in range(t):
    n = int(input())
    sum_of_multiples = calculate_sum_of_multiples(n)
    print(sum_of_multiples)





def calculate_sum_of_multiples(n):
    n -= 1 
    sum_of_multiples = 0
    sum_of_multiples += (3 * (n // 3) * (n // 3 + 1)) // 2 
    sum_of_multiples += (5 * (n // 5) * (n // 5 + 1)) // 2  
    sum_of_multiples -= (15 * (n // 15) * (n // 15 + 1)) // 2  
    return sum_of_multiples

t = int(input())

for i in range(t):
    n = int(input())
    sum_of_multiples = calculate_sum_of_multiples(n)
    print(sum_of_multiples)








