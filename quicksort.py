from random import randrange

def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i<=pivot]
        katta = [i for i in array if i>pivot]
        return qsort(kichik) + [pivot] + qsort(katta)
array = [22,15,17,19,45,16,39,85,72,64,49,147,258,369,963,852,741,456,654,951,753,82,456,789]
print(qsort(array))

def qsort2(array):
    if len(array) < 2:
        return array
    else:
        # pivot = array.pop(0)
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i <= pivot]
        katta = [i for i in array if i > pivot]
        # print(f"{kichik}+[{pivot}]+{katta}")
        return qsort2(kichik) + [pivot] + qsort2(katta)


if __name__ == '__main__':
    array1 = [1, 5, 12, 0, -5, 66]
    print(array1)
    print(qsort2(array1))
    array2 = list(range(20))
    print(array2)
    print(qsort2(array2))
    array3 = ['olma', 'anjir', 'shaftoli', 'qovun', 'tarvuz']
    print(array3)
    print(qsort2(array3))