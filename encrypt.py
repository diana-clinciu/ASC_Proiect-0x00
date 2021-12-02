import sys

key = sys.argv[1]
nume_fisier_input = sys.argv[2]
nume_fisier_output = sys.argv[3]

with open(nume_fisier_input, 'r') as f:
    text = f.read()

with open(nume_fisier_output, 'wb') as f:
    len_key = len(key)
    for i in range(len(text)):
        b = ord(text[i]) ^ ord(key[i % len_key])
        f.write(b.to_bytes(1, byteorder='big'))
