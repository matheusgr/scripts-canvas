import os
import os.path
import time

import requests
import links_from_header

from dotenv import load_dotenv


class CanvasError(Exception):
    pass


load_dotenv()

header = {'Authorization': 'Bearer ' + '%s' % os.getenv("TOKEN")}
canvas_url = os.getenv("URL") + '/' + os.getenv("COURSE_ID")


def put_data(addr, payload):
    url = canvas_url + '/' + addr
    r = requests.put(url, data=payload, headers=header)
    if r.status_code == 404:
        raise CanvasError("404 Not Found")
    data = r.json()
    print(data)

def post_data(addr, payload):
    url = canvas_url + '/' + addr
    r = requests.post(url, data=payload, headers=header)
    if r.status_code == 404:
        raise CanvasError("404 Not Found")
    data = r.json()
    print(data)

def get_data(addr, paginate=True):
    time.sleep(int(os.getenv("SLEEP_TIME")))
    url = canvas_url + '/' + addr
    r = requests.get(url, headers=header )
    if r.status_code == 404:
        raise CanvasError("404 Not Found")
    data = r.json()
    result = []
    if isinstance(data, (list, tuple)):
        result = list(data)
    else:
        result = [data]
    if not paginate:
        return result
    if 'Link' in r.headers:
        links = links_from_header.extract(r.headers['Link'])
        while 'next' in links:
            url = links['next']
            r = requests.get(url, headers=header )
            data = r.json()
            if isinstance(data, (list, tuple)):
                result.extend(data)
            else:
                result.append(data)
            links = links_from_header.extract(r.headers['Link'])
        
    return result
