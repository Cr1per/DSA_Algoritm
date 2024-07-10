def Bubble_sort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)


if __name__ == '__main__':
    array = [5,2,3,0,8,4,6,7,1]
    print(array)
    Bubble_sort(array)