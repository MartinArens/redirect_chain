#!/usr/bin/env python

import requests
import sys

url = sys.argv[1]


def get_redirect_chain(url):
    try:
        r = requests.get(url)

        if len(r.history) > 0:
            chain = ""
            code = r.history[0].status_code
            final = r.url
            for resp in r.history:
                chain += resp.url + " | "
            return str(code) + ' - ' + str(len(r.history)) + ' - ' + chain + ' - ' + final + ' - '
        else:
            return str(r.status_code)
    except requests.ConnectionError:
        print("Error")
        return '0'


print(get_redirect_chain(url))


