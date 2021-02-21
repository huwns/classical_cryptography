from bs4 import BeautifulSoup as bs

# Reference(https://www.google.co.jp/ime/-.-.html)
GOOGLE_MORSE = '''
<div class="morse-table">
          <h3>和文モールス符号表</h3>
          <table>
            <tbody><tr>
              <td>ア<span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td>イ<span><span class="dit"></span><span class="dah"></span></span></td>
              <td>ウ<span><span class="dit"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>エ<span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td>オ<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dit"></span></span></td>
            </tr>
            <tr>
              <td>カ<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>キ<span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>ク<span><span class="dit"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>ケ<span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td>コ<span><span class="dah"></span><span class="dah"></span><span class="dah"></span><span class="dah"></span></span></td>
            </tr>
            <tr>
              <td>サ<span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>シ<span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>ス<span><span class="dah"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>セ<span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>ソ<span><span class="dah"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span></td>
            </tr>
            <tr>
              <td>タ<span><span class="dah"></span><span class="dit"></span></span></td>
              <td>チ<span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>ツ<span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>テ<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td>ト<span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span></span></td>
            </tr>
            <tr>
              <td>ナ<span><span class="dit"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>ニ<span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>ヌ<span><span class="dit"></span><span class="dit"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>ネ<span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>ノ<span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span></span></td>
            </tr>
            <tr>
              <td>ハ<span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>ヒ<span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>フ<span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>ヘ<span><span class="dit"></span></span></td>
              <td>ホ<span><span class="dah"></span><span class="dit"></span><span class="dit"></span></span></td>
            </tr>
            <tr>
              <td>マ<span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>ミ<span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>ム<span><span class="dah"></span></span></td>
              <td>メ<span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>モ<span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span></span></td>
            </tr>
            <tr>
              <td>ヤ<span><span class="dit"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td></td>
              <td>ユ<span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td></td>
              <td>ヨ<span><span class="dah"></span><span class="dah"></span></span></td>
            </tr>
            <tr>
              <td>ラ<span><span class="dit"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>リ<span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>ル<span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>レ<span><span class="dah"></span><span class="dah"></span><span class="dah"></span></span></td>
              <td>ロ<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
            </tr>
            <tr>
              <td>ワ<span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>ヰ<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td></td>
              <td>ヱ<span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dit"></span></span></td>
              <td>ヲ<span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dah"></span></span></td>
            </tr>
            <tr>
              <td>ン<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>長音 (ー)<span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
              <td>濁点 (゛)<span><span class="dit"></span><span class="dit"></span></span></td>
              <td>半濁点 (゜)<span><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span></td>
              <td>区切り点 (、)<span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span><span class="dit"></span><span class="dah"></span></span></td>
            </tr><tr>
          </tr></tbody></table>
          <p class="morse-table-note">
            「っ」や「ゃゅょ」のような促音・拗音は、従来の和文モールス符号ではサポートされていませんが、Google 日本語入力モールスバージョンでは、大きい「つ」や「やゆよ」の後に半濁点符号<span class="signals"><span class="dit"></span><span class="dit"></span><span class="dah"></span><span class="dah"></span><span class="dit"></span></span>を打つことで、促音・拗音を入力することができます。
          </p>
        </div>
'''

def google_morse_parser(msg):
    parsed_dict = {}
    soup = bs(msg, 'html.parser')
    soup_td = soup.find('table').find_all('td')
    for i in soup_td:
        if i.text is not None:
            if '(' in i.text:
                key = i.text.split('(')[1].split(')')[0]
            else:
                key = i.text
            soup_span = i.find_all('span')
            value = ''
            for span in soup_span:
                dahdit = span.get('class')
                if dahdit == ['dah']:
                    value += '-'
                elif dahdit == ['dit']:
                    value += '.'
            parsed_dict[key] = value
    return parsed_dict