from my_function import caesar

text = 'This is the test.'
key = 11

ciphertext = caesar(text, key)
print(ciphertext)
plaintext = caesar(ciphertext, -key)
print(plaintext)