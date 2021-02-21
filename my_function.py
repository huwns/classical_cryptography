def inverse_dict(d):
    """キーと値を入れ替えた辞書を返す"""
    return {v:k for k,v in d.items()}

def slice_words(s,interval):
    """ある文字数ごとに切り分ける

    s: 対象文字列, interval: 切り分ける文字数"""
    return [s[i:i+interval] for i in range(0, len(s), interval)]

def caesar(text, key) -> str:
    """シーザー暗号の暗号化と復号

    暗号化: key, 復号: -key
    key: 0-25
    """
    ans = ''
    for s in text:
        if s.isupper():
            ans += chr(((ord(s) - ord('A') + key) % 26) + ord('A'))
        elif s.islower():
            ans += chr(((ord(s) - ord('a') + key) % 26) + ord('a'))
        else:
            ans += s
    return ans

def count_each_words(words) -> list:
    """文字列内の各アルファベットの出現回数を記録した辞書を降順で返す"""
    count_dic = {}
    for abc in string.ascii_lowercase:
        count_dic[abc] = words.count(abc)
    return sorted(count_dic.items(), key=lambda x:x[1], reverse=True)

def make_freq_dic(alphabet_frequency, count_dic) -> dict:
    """一般的なアルファベットの出現頻度を降順で並べたものと
    文字列内のある文字列内の各アルファベットの出現回数を記録した降順辞書とで
    各文字の対応付けをした辞書を返す"""
    freq_dic = {}
    for i, value in enumerate(count_dic):
        freq_dic[value[0]] = alphabet_frequency[i]
    return freq_dic

def dic_decrypt(encrypted_words, dic) -> str:
    """換字式暗号解読機

    辞書を元に文字を置き換え、暗号を解読する。"""
    decrypted_flag = ''
    for word in encrypted_words:
        if word in dic.keys():
            decrypted_flag += dic[word]
        else:
            decrypted_flag += word
    return decrypted_flag

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
