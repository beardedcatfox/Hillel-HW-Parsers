import urllib.parse as urlparser



def parse(query: str) -> dict:
    res = {}
    pars_res = urlparser.urlparse(query)
    dfq = pars_res.query
    dict_from_query = urlparser.parse_qs(dfq)
    for ind, val in dict_from_query.items():
        res.update({ind: str(*val)})
    return res



if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com/path/to/page?name=what?&color=hz') == {'name': 'what?', 'color': 'hz'}
    assert parse('https://example.com/path/to/page?name=AnastaSIIA&color=nope') == {'name': 'AnastaSIIA', 'color': 'nope'}
    assert parse('http://example.com/?who=idk') == {'who': 'idk'}
    assert parse('https://example.com/path/to/page?name=ferret&') == {'name': 'ferret'}
    assert parse('http://example.com/?12345=54321') == {'12345': '54321'}
    assert parse('http://example.com/?type=int') == {'type': 'int'}
    assert parse('http://example.com/?Happy=New_Year') == {'Happy': 'New_Year'}
    assert parse('http://example.com/path/to/about?name=surename') == {'name': 'surename'}
    assert parse('http://example.com/?contacts=number&map=link') == {'contacts': 'number', 'map': 'link'}
    assert parse('https://example.com/path/to/page?') == {}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
