import string

### 1.
def Uzunlik(text):
    if text == '':
        print("\nHech narsa kiritmadingiz Iltimos kiriting:")
    else:
        print(f"{text} ning uzunligi: {len(text)}")

uzunlik = input("So'zning uzunligini bilib beradi:\n[misol: Olma]: >>> ")
print(Uzunlik(uzunlik))

#### 2.
matn = list(string.ascii_lowercase)
def alfabit(text):
    return matn.index(text[0].lower())

alif = input("Birinchi harfning indexsini chiqarib beradi:\n>>> ")
print(alfabit(alif))

#### 3.
alfabit1 = list(string.ascii_lowercase)
tub = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101) # 26 ta tub son

def Son(text):
    sum=0
    for t in text.lower():
        sum += tub[alfabit1.index(t)]
    return sum%10

index = input("So'zni olib indexlarini qoshib 10 ga bo'lim chiqarib beradi:\n>>> ")
print(Son(index))















