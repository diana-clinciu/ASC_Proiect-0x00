import sys

key = sys.argv[1]
len_key = len(key)
nume_fisier_input = sys.argv[2]
nume_fisier_output = sys.argv[3]

with open(nume_fisier_input, 'rb') as f, open(nume_fisier_output, 'w') as g:
    byte = f.read(1)
    i = 0
    while byte:
        char = chr(int.from_bytes(byte, byteorder='big') ^ ord(key[i % len_key]))
        g.write(char)
        i = i+1
        byte = f.read(1)
