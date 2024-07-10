def fakratial(x):
    print(x,end=' ')
    if x == 1:
        return 1
    else:
        return x * fakratial(x-1)


print(fakratial(5))