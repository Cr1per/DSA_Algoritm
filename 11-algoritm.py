from pprint import pprint as print


binolar = ()
hududlar = ()
print(binolar)

yakuniy_binolar = set()
while hududlar:
    best_bino = None
    qamralgan_hududlar = set()
    for bino,bino_qamrovi in binolar.items():
        qamrov = hududlar & bino_qamrovi
        print(f"{bino}:{qamrov}")
        if len (qamrov)>len(qamralgan_hududlar):
            best_bino = bino
            qamralgan_hududlar = qamrov
    hududlar -= qamralgan_hududlar
    yakuniy_binolar.add(best_bino)
    print(f"tanlangan bino:{best_bino}")
    print(f"hududlar:{hududlar}")
    print(f"yakuniy bino:{yakuniy_binolar}")
    input()