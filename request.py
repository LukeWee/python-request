

import requests

url=('http://www.thestar.com.my/',
     'http://www.ebay.com/',
     'https://www.facebook.com/',
     'https://www.youtube.com/',
     'https://www.netflix.com/',
     'http://www.chinapress.com.my/',
     'http://www.yahoo.com/',
     'http://www.google.com/',
     'https://www.bing.com/',
     'https://www.lelong.com.my/')

for count in range(0,9):
    r = requests.get(url[count], auth=('user', 'pass'))

    print (r.status_code)
    print (r.headers['content-type'])
    print (r.encoding)
    print (r.text)
    try:
        print (r.json())
        
    except ValueError:
        print r
