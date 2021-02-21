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

if __name__ == '__main__':
    # example: rot13
    encrypted_text = caesar('This is the test.', 13)
    print(encrypted_text)
    print(caesar(encrypted_text, 13))
