from collections import deque

def search(start_node,target='elon musk'):
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f"{target}ni topdik!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

if __name__ == '__main__':
    graph = {'siz':['ali','vali','tohir'],
             'ali':['aziza','olim'],
             'vali':['botir','ziyoda'],
             'tohir':['elon musk','mohir'],
             'aziza':[],
             'olim':[],
             'botir':[],
             'ziyoda':['aziza'],
             'elon musk':[],
             'mohir':[]}
    search('siz', 'elon mask')



graph1={
    'A':{'B':2, 'C':6},
    'B':{'C':3, 'D':4},
    'C':{'D':5, 'E':6},
    'D':{'F':5},
    'E':{'F':0},
    'F':{} }
print(graph1)

narxlar = {
    'B': 2,
    'C': 6,
    'D': float('inf'),
    'E': float('inf'),
    'F': float('inf') }
otalar = {
    'B': 'A',
    'C': 'A',
    'D': None,
    'E': None,
    'F': None,  }


##Eng arzon tugun topish uchun funksiya
ishlandi = []
def eng_arzon_tugun_top(narxlar):
    eng_arzon = float('inf')
    eng_arzon_tugun = None
    for tugun in narxlar:
        narx = narxlar[tugun]
        if narx < eng_arzon and tugun not in ishlandi:
            eng_arzon = narx
            eng_arzon_tugun = tugun
    return eng_arzon_tugun

print(narxlar)
tugun = eng_arzon_tugun_top(narxlar)
print(f"Eng arzon tugun: {tugun}")

##Dijkstra Algoritmi kodi
tugun = eng_arzon_tugun_top(narxlar) # A nuqtaga eng arzon tugundan boshlaymiz
print(tugun)

while tugun is not None:
    qoshnilar = graph1[tugun] # Eng yaqin tugunning qo'shnilarini topamiz
    narx = narxlar[tugun] # Ularning narxini olamiz
    for qoshni in qoshnilar.keys(): # Har bir qo'shni uchun...
        yangi_narx = narx + qoshnilar[qoshni] # shu qo'shniga borish narxini hisoblaymiz
        if narxlar[qoshni]>yangi_narx: # agar bu tugunga borish avvalgidan arzonroq bo'lsa:
            narxlar[qoshni] = yangi_narx # shu tugunga borish narxini yangilaymiz
            otalar[qoshni] = tugun # va bu tugun otasini ham yangilaymiz.
    ishlandi.append(tugun) # tugunn ishlov berilgan tugunlar qatoriga qo'shamiz
    tugun = eng_arzon_tugun_top(narxlar)

print(narxlar)