# -*- coding:utf-8 -*-

import requests
import base64
from query.util.proxy import ProxyMiddleware

cookie = '_vwo_uuid_v2=DBB13BA22B0C1EB67D9CE274EFE72356C|960ce612200358345b496a73a96e17bc; ' \
         'douban-fav-remind=1; gr_user_id=23e95ede-de53-4fff-a060-ed1baaa34c86; bid=pKAKTfSOTBE; ' \
         'll="118240"; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.1897782509.1526105576; ' \
         'douban-profile-remind=1; ps=y; viewed="4666490_4866934_27108478_25730741_26919485_247' \
         '19824_1807887_6551147_1403307_1764076"; __utma=30149280.1897782509.1526105576.1586574998.1' \
         '586741654.181; __utmz=30149280.1586741654.181.142.utmcsr=baidu|utmccn=(organic)|utmcmd=organi' \
         'c; __utmc=30149280; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1586741676%2C%22https' \
         '%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D57aywD0Q6WTnl7XKbIHuEzg3thMUswU0N7WVgfgfFaoK3nkT99djGQ' \
         'UKJn5NmTLthzagWNfatEkX7kLQ3tW9RK%26wd%3D%26eqid%3D91fffbf2001869bb000000025e93c1a6%22%5D; _' \
         'pk_ses.100001.4cf6=*; __utmc=223695111; __utmb=223695111.0.10.1586743055; __utma=223695111.' \
         '1594964971.1526105576.1586741676.1586743055.116; __utmz=223695111.1586743055.116.94.utmcsr' \
         '=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; dbcl2="188919931:dOq3sjpu' \
         'nlE"; ck=JoU4; __utmt=1; __utmv=30149280.18891; __utmb=30149280.10.9.1586743294295; _pk_id' \
         '.100001.4cf6=6b37c4bebb42df17.1526105576.113.1586743470.1586227468.'

cookieDict = {}
cookies = cookie.split("; ")
for line in cookies:
    key, value = line.split('=', 1)
    cookieDict[key] = value

ua_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}

Proxy = ProxyMiddleware()
proxy = Proxy.getProxy()
def get_Image_with_proxy(url,proxy):
    print('---启用代理----')
    print(proxy)
    try:
        res = requests.get(url,proxies={'http':str(proxy)},headers = ua_headers)
        res.encoding = 'utf-8'
        if len(res.content) > 700 :
            with open('tmp.jpg', 'wb') as f:
                f.write(res.content)
            with open("tmp.jpg", "rb") as f:
                base64_data = base64.b64encode(f.read())
            return base64_data.decode('utf-8')
        else:
            Proxy.changeProxy()
            newproxy = Proxy.getProxy()
            get_Image_with_proxy(url,newproxy)
    except:
        return None

def getImage(url):
    try:
        res = requests.get(url, headers = ua_headers, cookies=cookieDict)
        res.encoding = 'utf-8'

        if len(res.content) > 700 :
            with open('tmp.jpg','wb') as f:
                f.write(res.content)

            with open("tmp.jpg", "rb") as f:
                base64_data = base64.b64encode(f.read())
            return base64_data.decode('utf-8')
        else:
            return get_Image_with_proxy(url,proxy)
    except:
        return None
if __name__ == '__main__':
    url = "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1910813120.webp"
    print(getImage(url))