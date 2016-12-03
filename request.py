

import requests;

r = requests.get('https://sg.yahoo.com/?p=us', auth=('user', 'pass'));

print (r.status_code);
print (r.headers['content-type']);
print (r.encoding);
print (r.text);
print (r.json());

