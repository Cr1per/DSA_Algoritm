def linear_search(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None

List1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
print(linear_search(List1,23))


