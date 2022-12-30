<<<<<<< HEAD
def parse(query: str) -> dict:
    return {}
=======
import re

def parse(query: str) -> dict:
    myd = dict()
    if 'name' in query:
        myd['name'] = re.search(r'name=(\w+)', query).group(1)
    if 'color' in query:
        myd['color'] = re.search(r'color=(\w+)', query).group(1)
    return myd
>>>>>>> 5d27e753a872f3c42e7753a16000ec9ea463900b


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

<<<<<<< HEAD

def parse_cookie(query: str) -> dict:
    return {}
=======
    assert parse('https://example.com/path/to/page?name=Pavel&color=green') == {'name': 'Pavel', 'color': 'green'}
    assert parse('https://example.com/path/to/page?name=test&color=_') == {'name': 'test', 'color': '_'}
    assert parse('https://example.com/path/to/page?name=MaxKol&color=Blue') == {'name': 'MaxKol', 'color': 'Blue'}
    assert parse('https://example.com/path/to/page?name=oLena&color=deepPurple') == {'name': 'oLena', 'color': 'deepPurple'}
    assert parse('https://example.com/path/to/page?name=Hillel&color=deep_green') == {'name': 'Hillel', 'color': 'deep_green'}
    assert parse('https://example.com/path/to/page?name=Anastasiia&color=rose') == {'name': 'Anastasiia', 'color': 'rose'}
    assert parse('https://example.com/path/to/page?name=pEdRo&color=wHite') == {'name': 'pEdRo', 'color': 'wHite'}
    assert parse('https://example.com/path/to/page?name=A_Joe&color=red') == {'name': 'A_Joe', 'color': 'red'}
    assert parse('https://example.com/path/to/page?name=AKoel&color=purple') == {'name': 'AKoel', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=okey&color=black') == {'name': 'okey', 'color': 'black'}


def parse_cookie(query: str) -> dict:
    myd = dict()
    if 'name' in query:
        myd['name'] = name = re.search(r'name=((\w+=?)+)', query).group(1)
    if 'age' in query:
        myd['age'] = re.search(r'age=(\w+)', query).group(1)
    return myd

>>>>>>> 5d27e753a872f3c42e7753a16000ec9ea463900b


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
<<<<<<< HEAD
=======

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
>>>>>>> 5d27e753a872f3c42e7753a16000ec9ea463900b
