n = 5000
lst = []

def int_to_octal(n):
    while n != 0:
        r = n%8
        lst.append(r)
        n = n //8
    
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end="")

int_to_octal(n)