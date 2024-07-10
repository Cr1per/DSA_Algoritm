##array elementlarini sonini chiqaradi
def array(list):
    return 0 if not list else 1 + array(list[1:])

list = [1, 2, 3, 4, 5]
print(f"Array elementlari soni: {array(list)}")

## arrayni eng katta elementini qaytaruvchi funk
def max_element(list):
    if len(list) == 1:
        return list[0]

    m = len(list) // 2
    l = max_element(list[:m])
    r = max_element(list[m:])

    return l if l > r else r

list = [1, 2, 3, 4, 5]
print(f"Arrayning eng katta elementi: {max_element(list)}")

### Binary Search qidirish algoritmi:
# def binary_search(list, t, l=0, h=None):
#     if h is None:
#         h = len(list) - 1
#     if l > h:
#         return -1
#     m = (l + h) // 2
#     if list[m] == t:
#         return m
#     elif list[m] < t:
#         return binary_search(l, t, m + 1,h)
#     else:
#         return binary_search(list, t, l,m - 1)
# list = [1, 2, 3, 4, 5]
# t = 3
# i = binary_search(list, t)
# print(f"{t} elementi indexi: {i}")