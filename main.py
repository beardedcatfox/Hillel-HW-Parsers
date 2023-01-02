import urllib.parse as urlparser
from http.cookies import SimpleCookie

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
    ck = SimpleCookie()
    ck.load(query)
    cookies = {a: b.value for a, b in ck.items()}
    return cookies



if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('today=New_Year;num=2023') == {'today': 'New_Year', 'num': '2023'}
    assert parse_cookie('123=321;456=abc;') == {'123': '321', '456': 'abc'}
    assert parse_cookie('1=2=3=4;True=False;') == {'1': '2=3=4', 'True': 'False'}
    assert parse_cookie('name=unname;age=inf;sex=male') == {'name': 'unname', 'age': 'inf', 'sex': 'male'}
    assert parse_cookie('one=1;two=2;three=3;four=4;') == {'one': '1', 'two': '2', 'three': '3', 'four': '4'}
    assert parse_cookie('k,ymjhf;tkdhgbcn') == {}
    assert parse_cookie('gjvhggnv,gmhng') == {}
    assert parse_cookie('??????;;') == {}
    assert parse_cookie('SCHOOL=HILLEL;COURSE=PYTHON_PRO;') == {'SCHOOL': 'HILLEL', 'COURSE': 'PYTHON_PRO'}
    assert parse_cookie('name=!!!;!!!=28') == {'name': '!!!', '!!!': '28'}
    assert parse_cookie('a=b;c=d;') == {'a': 'b', 'c': 'd'}
    assert parse_cookie('!/??ef;.,lmlvlv,') == {}

