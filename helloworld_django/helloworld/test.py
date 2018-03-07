import requests
from sure import expect
from httpretty import HTTPretty, httprettified
from httpretty.compat import text_type
from httpretty.core import decode_utf8

@httprettified
def test_GET_no_accept_header(now):
    "Should return hello world message"

    HTTPretty.register_uri(HTTPretty.GET, "http://127.0.0.1:8000/",
                           body="<p>Hello, world!</p>",
                           status=200)

    response = requests.get('http://github.com/')
    expect(response.status_code).to.equal(200)

    expect(dict(response.headers)).to.equal({
        'content-type': 'text/html; charset=utf-8',
        'status': '200'
    })

def test_GET_with_accept_header(now):
    "A request with an application/json Accept header should return a good morning message in json"

    HTTPretty.register_uri(HTTPretty.GET, "http://127.0.0.1:8000/",
                           body='{"message": "Good morning"}',
                           forcing_headers={
                               'Accept': 'application/json'
                           },
                           status=200)
    expect(response.status_code).to.equal(200)
    response = requests.get('http://127.0.0.1:8000/', headers={"accept":"application/json"})
    expect(response.text).to.equal('{"message": "Good morning"}')