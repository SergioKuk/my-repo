import requests

fname = 'dataset_3378_3.txt'
with open(fname,'r') as f:
    url = f.readline().strip()
plist = url.split('/')
rm = plist[-1]
plist.remove(rm)
print (plist)
path = ''
for i in plist:
    path += i + '/'
print(path)
cnt = 0
print(url)
while cnt<1000:
    cnt += 1
    getf = requests.get(url)
    txt = getf.text.split()
    # print(txt)
    if txt[0] == 'We':
        print(getf.text)
        print(cnt)
        break
    else:
        url = path+getf.text
    print(url)

