# vigenere_test.py

from my_function import vigenere_encrypt, vigenere_decrypt

plaintext = 'Who\'s Mary? Where\'s John? I\'m Shelock Holmes!'
key = 'MORIARTY'
ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)
m = vigenere_decrypt(ciphertext, key)
print(m)