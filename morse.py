from jaconv import hira2kata
import re, unicodedata
from winsound import Beep
from time import sleep

MORSE_DICT ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    "." : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "?" : "..--..",
    "'" : ".----.",
    "-" : "-....-",
    "/" : "-..-.",
    "@" : ".--.-.",
    "=" : "-...-",
    "!" : "-.-.--"
}

MORSE_DICT_JP = {
    'ア' : '--.--',
    'カ' : '.-..',
    'サ' : '-.-.-',
    'タ' : '-.',
    'ナ' : '.-.',
    'ハ' : '-...',
    'マ' : '-..-',
    'ヤ' : '.--',
    'ラ' : '...',
    'ワ' : '-.-',
    'イ' : '.-',
    'キ' : '-.-..',
    'シ' : '--.-.',
    'チ' : '..-.',
    'ニ' : '-.-.',
    'ヒ' : '--..-',
    'ミ' : '..-.-',
    'リ' : '--.',
    'ヰ' : '.-..-',
    'ウ' : '..-',
    'ク' : '...-',
    'ス' : '---.-',
    'ツ' : '.--.',
    'ヌ' : '....',
    'フ' : '--..',
    'ム' : '-',
    'ユ' : '-..--',
    'ル' : '-.--.',
    'ン' : '.-.-.',
    'エ' : '-.---',
    'ケ' : '-.--',
    'セ' : '.---.',
    'テ' : '.-.--',
    'ネ' : '--.-',
    'ヘ' : '.',
    'メ' : '-...-',
    'レ' : '---',
    'ヱ' : '.--..',
    'オ' : '.-...',
    'コ' : '----',
    'ソ' : '---.',
    'ト' : '..-..',
    'ノ' : '..--',
    'ホ' : '-..',
    'モ' : '-..-.',
    'ヨ' : '--',
    'ロ' : '.-.-',
    'ヲ' : '.---',
    '゛' : '..',
    '゜' : '..--.',
    '。' : '.-.-..',
    'ー' : '.--.-',
    '、' : '.-.-.-',
    '（' : '-.--.-',
    '）' : '.-..-.',
    '？' : '..--..',
    '！' : '-.-.--'
}

def morse_encode(msg, morse_dict) -> list:
    encoded_lst = []
    for i in msg.upper():
        if i in morse_dict:
            encoded_lst.append(morse_dict.get(i))
        else:
            encoded_lst.append('[ERROR]')
            print('ERROR: ', i, 'is not in the dictionary.')
    return ' '.join(encoded_lst)

def morse_decode(msg, morse_dict) -> str:
    decoded_msg = ''
    reverse_morse_dict = dict((v,k) for (k,v) in morse_dict.items())
    for i in msg.split(' '):
        if i in reverse_morse_dict:
            decoded_msg += reverse_morse_dict.get(i)
        else:
            decoded_msg += '[ERROR]'
            print('ERROR: ', i, 'is not in the dictionary.')
    return decoded_msg

def dakuten_separator(msg):
    bytes_text = unicodedata.normalize('NFD', msg).encode()
    bytes_text = re.sub(b'\xe3\x82\x99', b"\xe3\x82\x9b", bytes_text)
    bytes_text = re.sub(b"\xe3\x82\x9a", b'\xe3\x82\x9c', bytes_text)
    return bytes_text.decode()

def morse_sound(morse):
    for i in morse:
        if i == '-':
            Beep(300, 75*3)
        elif i == '.':
            Beep(300, 75)
        else:
            sleep(0.075)

def morse_test(msg, morse_dict):
    msg = dakuten_separator(hira2kata(msg))
    encoded_msg = morse_encode(msg, morse_dict)
    print(encoded_msg)
    decoded_msg = morse_decode(encoded_msg, morse_dict)
    print(decoded_msg)
    morse_sound(encoded_msg)

if __name__ == '__main__':
    morse_test("What's up?", MORSE_DICT)
    morse_test('よう！げんき？', MORSE_DICT_JP)
