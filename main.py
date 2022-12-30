import re

def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    myd = dict()
    if 'name' in query:
        myd['name'] = name = re.search(r'name=((\w+=?)+)', query).group(1)
    if 'age' in query:
        myd['age'] = re.search(r'age=(\w+)', query).group(1)
    return myd


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    
    assert parse_cookie('name=pavel;age=23;') == {'name': 'pavel', 'age': '23'}
    assert parse_cookie('name=oLeks;age=248;') == {'name': 'oLeks', 'age': '248'}
    assert parse_cookie('name=max_core;age=18;') == {'name': 'max_core', 'age': '18'}
    assert parse_cookie('name=tEsT;age=1128;') == {'name': 'tEsT', 'age': '1128'}
    assert parse_cookie('name=aaaa;age=22;') == {'name': 'aaaa', 'age': '22'}
    assert parse_cookie('name=AnastasiiaSU;age=28;') == {'name': 'AnastasiiaSU', 'age': '28'}
    assert parse_cookie('name=QA;age=88;') == {'name': 'QA', 'age': '88'}
    assert parse_cookie('name=Max_Min;age=1;') == {'name': 'Max_Min', 'age': '1'}
    assert parse_cookie('name=AAAAA;age=0;') == {'name': 'AAAAA', 'age': '0'}
    assert parse_cookie('name=S=D=F;age=000;') == {'name': 'S=D=F', 'age': '000'}

