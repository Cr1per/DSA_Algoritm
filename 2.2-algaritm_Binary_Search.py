def binary_search(list, item):
    l = 0
    h = len(list)-1
    while l <= h:
        m = (l + h)//2
        guess = list[m]
        if guess == item:
            return m
        if guess > item:
            h = m - 1
        else:
            l = m + 1
    return None
List1 = [1,3,4,6,7,8,10,12,23]
print(binary_search(List1,7))

