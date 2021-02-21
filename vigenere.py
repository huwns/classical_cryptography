def vigenere_encrypt(plaintext, key):
    """Vigenere Cipher Encrypt

    key are only UPPERCASE ALPHABET[A-Z]."""
    count = 0
    ciphertext = ''
    key = key.upper()
    for s in plaintext:
        if s.isupper():
            ciphertext += chr(((ord(s) + ord(key[count % len(key)])) % 26) + ord('A'))
        elif s.islower():
            ciphertext += chr(((ord(s) + ord(key[count % len(key)]) - (ord('a') - ord('A'))) % 26) + ord('a'))
        else:
            ciphertext += s
        count += 1
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Vigenere Cipher Decrypt

    key are only UPPERCASE ALPHABET[A-Z]."""
    count = 0
    plaintext = ''
    key = key.upper()
    for s in ciphertext:
        if s.isupper():
            plaintext += chr(((ord(s) - ord(key[count % len(key)])) % 26) + ord('A'))
        elif s.islower():
            plaintext += chr(((ord(s) - ord(key[count % len(key)]) - (ord('a') - ord('A'))) % 26) + ord('a'))
        else:
            plaintext += s
        count += 1
    return plaintext

if __name__ == '__main__':
    plaintext = 'Who\'s Mary? Where\'s John? I\'m Shelock Holmes!'
    key = 'MORIARTY'
    ciphertext = vigenere_encrypt(plaintext, key)
    print(ciphertext)
    print(vigenere_decrypt(ciphertext, key))