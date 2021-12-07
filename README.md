# Cripaterea XOR
Echipa noasta: ADA

Echipa adversa: Velociraptor

Cheia echipei adverse: velociraptor69

## Modul de apelare encrypt.py/decrypt.py:
Apelare encrypt: python encrypt.py (Parola) (input) (output)

Apelare decrypt: python encrypt.py (Parola) (input) (output)


## Aflarea parolei echipei adverse:
### Prima parte (daca stim si input-ul): 

***Codul efectiv il gasiti in partea1.py.***

:lemon:_"Easy peasy lemon squeezy"_:lemon:: Se xor-eaza cele doua fisiere (input.txt si output) si rezulta cheia.

De ce merge?

Ne folosim de relatia:

      a ^ (a ^ b) = a ^ a ^ b = 0 ^ b = b 
      
Astfel,

      input ^ output = input ^ (input ^ cheie) = input ^ input ^ cheie = 0 ^ cheie = cheie
  

### A doua parte (fara input): 

#### Metoda 1)    Brute Force: 

***Codul efectiv il gasiti in partea2.py.***

Ca sa aflam cheia va trebui sa divizam problema in doua parti. 

##### Partea 1: Aflam lungimea cheii.
1. Luam pe rand toate lungimile posibile (de la 10 la 15).
2. Pentru lungimea L aleasa construim blocuri de lungime L cu caracterele din text. Nu trebuie sa spargem tot textul in blocuri, ne trebuie doar cateva. (noi am ales 10, dar mergeau si mai putine) 
3. Calculam distanta Hamming dintre toate blocurile cu lungimea L aleasa.

      Dar, de ce? Distanta Hamming ne spune cat de "asemanatoare" sunt blocurile. Cu cat mai asemanatoare, cu atat avem sanse mai mari sa fi ales lungimea adevarata a cheii (pt ca ce  face blocurile asemanatoare este faptul ca au fost xor-uite cu caracterele cheii)
      
4. Insumam distantele Hamming si le impartim la L. Astfel, obtinem un "scor hamming" dupa care putem alege lungimea cea mai probabila.
5. Lungimea adevarata a cheii este cea care are "scor hamming" cat mai mic. 

##### Partea 2: Aflam caracterele cheii
1. Facem alte blocuri cu caracterele din output care au fost xor-ate cu aceeasi litera din cheie. Astfel, primul bloc e blocul caracterelor xor-ate cu prima litera din cheie, al doilea bloc e blocul caracterelor xor-ate cu a doua litera din cheie a.s.m.d. Acum ne mai ramane sa aflam cu ce caracter a fost xor-at fiecare bloc. 
2. Parcugem blocurile.
3. Incercam pe rand fiecare caracter posibil, descifram blocul cu el si vedem care da cel mai "romanesc" text.
      
Dar cum decidem cat de "romanesc" e un text? 
     
O sa ne folosim de frecventa literelor din romana si de "Fitting Quotient". Un text e mai "romanesc" cu cat frecventa literelor sale se apropie de cea a limbii romane. Ca sa masuram aceasta apropiere calculam "Fitting Quotient"-ul, care are formula:

![CodeCogsEqn](https://user-images.githubusercontent.com/95150057/145079205-39b92241-ae0b-4280-b0b6-5885636791ad.gif)

fi  = frecv. carct. i in text

f'i = frecv. carct. i in romana

n   = numar de litere in romana

4. Se calculeaza frecventa literelor din blocul decriptat si suma de sus.
5. Se alege caracterul care da "fitting quotient"-ul cel mai mic.

GATA!!          

#### Metoda 2)  Mai empirica ^^
Metoda de decriptare utilizata este una empirica si a mers deoarece parola a fost slaba.

Dupa cateva cautari pe google, am descoperit ca exista libraria de python pwntools si ca merge pe ubuntu. Am instalat python3 si am dat import la librarie, ne-am folosit de pwn.xor(parametru1, parametru2) pentru a xora fisierul de output cu diferite string-uri.

Printre primele lucruri incercate, a fost si numele echipei: velociraptor.

La fiecare parola incercata, am analizat primele 10-15 caractere, deoarece acolo se xora corect, indiferent de lungimea parolei.

Dupa ce am observat ca pentru "velociraptor" primele 12 caractere din rezultatul output^parola sunt "Din soseaua ", am continuat sa adaug caractere, ca sa determin lungimea exacta a parolei. Dupa ce am mai adaugat 2 caractere la stringul "velociraptor", am observat ca incep sa mai apara alte secvente in romana (urmatoarea secventa a fost " vine de la ").

Acum stim ca din parola lipsesc doar 2 caractere. Dupa ce am incercat "velociraptorii" si nu a mers, am trecut la numere.

Din moment ce lipseau doar doua caractere, insemna ca aveam de incercat maxim 99 de numere.

Le-am luat pe rand, de la 01 si am mers pana la numarul 69, unde textul era cel mai inteligibil.

Cum textul decriptat inca avea pasaje ciudate, m-am decis sa nu renunt la parola "velociraptor69".

Am luat si am cautat in fisierele lor de pe github, iar in manage.py, in variabila password, era un sting hash-uit.

Am luat parola gasita si am introdus-o intr-un hash generator si am luat fiecare metoda de hashing si am comparat-o cu ce am gasit in fisier.

Dupa verificare, am realizat ca parola lor era hashuita printr-un SHA-2(Secure Hash Algorithm 2), iar hash-ul generat si cel din manage.py erau identice.

Am ajuns la concluzia ca parola lor este "velociraptor69".

Codul de python pe care l-am folosit in ubuntu este:

      import pwn
      a=open('output').read()
      pwn.xor(a,"velociraptor69")

(rezultatul il citeam din terminal)

## Resurse:
Pentru metoda "brute force": 

https://idafchev.github.io/crypto/2017/04/13/crypto_part1.htmt 

https://arpitbhayani.me/blogs/decipher-single-xor

http://www.cryptogram.org/downloads/words/frequency.html (de unde am luat frecventele caracterelor in romana)
