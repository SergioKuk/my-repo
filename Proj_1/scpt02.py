

import requests

# r = requests.get('http://cisco.com')
# print(r.text)

#url = 'http://iptraffic.ru'
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
#par = {'key1':'value1', 'key2':'value2'}
#r = requests.get(url,params=par)
r = requests.get(url)
print(r.url)
print("\n\n",r.text)
print('\n\n',r.cookies)
