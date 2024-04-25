n = 23
lst = []

def bin_to_dec(n):
    while n != 1:
        r = n%2
        lst.append(r)
        n = n //2

    lst.append(1)
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end="")

bin_to_dec(n)
