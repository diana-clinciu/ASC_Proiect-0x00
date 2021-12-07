import sys

def distanta_Hamming(block1, block2):
    b1 = int.from_bytes(block1, byteorder='big')
    b2 = int.from_bytes(block2, byteorder='big')
    return bin(b1 ^ b2).count('1')


def cheie_sort(t):
    return t[1]
def lungime_posibila_cheie(text, nr_blocuri):
    lungimi_posibile = []
    for lung in range(10, 16):
        blocks = [[text[i] for i in range(x*lung, (x+1)*lung)] for x in range(nr_blocuri)]
        n = len(blocks)
        suma_ham = 0
        nr = 0
        for i in range(n-1):
            for j in range(i+1, n):
                suma_ham += distanta_Hamming(blocks[i], blocks[j])
                nr += 1
        medie = suma_ham/nr
        lungimi_posibile.append((lung, medie/lung))
    lungimi_posibile.sort(key=cheie_sort)
    return lungimi_posibile


frecv_ro = {'a': 16.31 + 0.808369+1.36313,      'b': 0.87177,       'c': 4.73926,           'd': 2.02885,
            'e': 11.0002,                       'f': 1.47408,       'g': 0.665716,          'h': 0.126803,
            'i': 11.3489+1.36313,               'j': 0.142653,      'k': 0,                 'l': 8.5275,
            'm': 2.64701,                       'n': 5.15137,       'o': 3.32858,           'p': 2.15565,
            'q': 0,                             'r': 6.4511,        's': 3.12252+1.28388,   't': 6.34015+0.253606,
            'u': 7.32287,                       'v': 1.52164,       'w': 0,                 'x': 0.0158504,
            'y': 0,                             'z': 0.348708,
            }


def afla_fracventa(text):
    d = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    for char in text:
        if char.isalpha():
            d[char.lower()] = d[char.lower()]+1
    for char in d:
        d[char.lower()] = d[char.lower()]/len(text)*100
    return list(d.values())


def fitting_quotent(frecv_ro, frecv_txt):
    S = 0
    for i in range(len(frecv_ro)):
        S += abs(frecv_ro[i]-frecv_txt[i])
    return S/26


def decripteaza(text, cheie):
    rez = ''.join([chr(char ^ ord(cheie)) for char in text])
    return rez



nume_fisier = sys.argv[1]

with open(nume_fisier, 'rb') as f:
    text = f.read()

lungime_cheie = lungime_posibila_cheie(text, 10)[0][0]

blocuri_transpuse = [list(text[i::lungime_cheie]) for i in range(lungime_cheie)]

caract_chei = [chr(x) for x in range(ord("a"), ord("z")+1)]
caract_chei.extend(chr(x).upper() for x in range(ord("a"), ord("z")+1))
caract_chei.extend("1234567890")

PAROLA = []
frecv_ro = list(frecv_ro.values())
print("Dureaza ceva....")
for bloc in blocuri_transpuse:
    MIN = float('inf')
    for i in caract_chei:
        text_bloc = decripteaza(bloc, i)
        frecv_actuala = afla_fracventa(text_bloc)
        if MIN > fitting_quotent(frecv_ro, frecv_actuala):
            MIN = fitting_quotent(frecv_ro, frecv_actuala)
            cheie_corecta = i
    PAROLA.append(cheie_corecta)

PAROLA = ''.join(PAROLA)
print(f"PAROLA ESTE: {PAROLA}!! :D")