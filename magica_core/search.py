import urllib.request, urllib.parse
import json


def search(query, **kwargs):
    apikey = "<APIKEY>"
    SEARCH_BASE = "http://apis.daum.net/search/book"

    kwargs.update({
        'apikey': apikey,
        'q': query,
        'output': 'json'
    })

    url = "{0}?{1}".format(SEARCH_BASE, urllib.parse.urlencode(kwargs))
    result = json.load(urllib.request.urlopen(url))
    return result
