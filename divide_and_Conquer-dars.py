###Ayirish
def ekub_ayirish(a, b):
    if a == b:
        return a
    return ekub_ayirish(a - b, b) if a > b else ekub_ayirish(a, b - a)

a = 45
b = 27
natija = ekub_ayirish(a, b)
print(f"{a} va {b} sonlarining EKUBi:  {natija}")

####2. Bo'lish
def ekub_bolish(a, b):
    return a if b == 0 else ekub_bolish(b, a % b)

a = 45
b = 27
natija = ekub_bolish(a, b)
print(f"{a} va {b} sonlarining EKUBi: {natija}")













