import re

def parse(query: str) -> dict:
    myd = dict()
    if 'name' in query:
        myd['name'] = re.search(r'name=(\w+)', query).group(1)
    if 'color' in query:
        myd['color'] = re.search(r'color=(\w+)', query).group(1)
    return myd


if __name__ == '__main__':
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

