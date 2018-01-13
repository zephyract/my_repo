import requests
import time

url = 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id=201720182002292&xkzy=&trjf='

head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/comeInGgxxkxk',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'JSESSIONID=jwms2~3DD779A8DD9F9A4C59268317CC9A5DBC'}

while True:
    try:
        res = requests.get(url, headers = head)
        print res.content
        if 'true' in res.content:
            break
        else:
            time.sleep(0.5)
    except:
        continue
