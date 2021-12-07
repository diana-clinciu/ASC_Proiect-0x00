# Cripaterea XOR
Echipa noasta: ADA

Echipa adversa: Velociraptor

Cheia echipei adverse: velociraptor69

## Modul de apelare encrypt.py/decrypt.py:
Apelare encrypt: python encrypt.py (Parola) (input) (output)

Apelare decrypt: python encrypt.py (Parola) (input) (output)


## Aflarea parolei echipei adverse:
### Prima parte (daca stim si input-ul): 

_"Easy peasy lemon squeezy"_: Se xor-eaza cele doua fisiere (input.txt si output) si rezulta cheia.

De ce merge?

Ne folosim de ralatia:

      a ^ (a ^ b) = a ^ a ^ b = 0 ^ b = b 
      
Astfel,

      input ^ output = input ^ (input ^ cheie) = input ^ input ^ cheie = 0 ^ cheie = cheie
  

### A doua parte (fara input, noroc cu criptopals): 

Brute Force: 
