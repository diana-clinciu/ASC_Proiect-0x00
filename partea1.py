with open("input.txt",'r') as f, open("output",'rb') as g, open("parola.txt",'x') as h:
    parola=[chr(ord(a) ^ b) for a,b in zip(f.read(15),g.read(15))]
    parola=''.join(parola)
    h.write(parola)