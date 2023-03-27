def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return n*fact(num-1)


n = int(input("enter the number:"))
print(fact(n))
