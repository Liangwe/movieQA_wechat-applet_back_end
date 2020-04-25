from time import sleep
import requests

ua_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}

class ProxyMiddleware():
    def __init__(self):
        # 调用代理API获取IP
        self.get_url = "http://ip.memories1999.com/api.php?dh=940868768473483234&sl=3"
        # 我们构建的IP池,用于存储从代理API中获取的IP
        self.ip_list = []
        # 记录当前使用的 ip 是IP池中的哪一个
        self.ip_count = 0
        # 最大请求数
        self.max_count = 3

        self.proxypath = "query/util/proxy.txt"

        with open(self.proxypath, "r", encoding='utf-8') as f1:
            lines = f1.readlines()  # 读取全部内容 ，并以列表方式返回
            for line in lines:
                if line != '\n':
                    self.ip_list.append(line.strip())

    def getIPData(self):
        """
        使用 requests 库去调用代理API获取IP,同时,将所有的 IP 存储到 IP 池  ip_list 中.
        """
        self.ip_list.clear()
        res = requests.get(self.get_url,headers=ua_headers)
        with open(self.proxypath,'w',encoding='utf-8') as f:
            f.write(res.text)
        # 填充IP池(这里的处理方法对于不同的代理而言,使用的函数不一样,但是本质都是一样的, 取出IP,填充)
        with open(self.proxypath, "r", encoding='utf-8') as f1:
            lines = f1.readlines()  # 读取全部内容 ，并以列表方式返回
            for line in lines:
                if line != '\n':
                    self.ip_list.append(line.strip())

    def getProxy(self):
        if self.ip_list != [] and self.ip_count < self.max_count:
            return self.ip_list[self.ip_count]
        else:
            return self.run()

    def changeProxy(self):
        self.ip_count += 1
        return self.ip_count

    def run(self):
        # ip池为空,我们现在需要先获得代理IP
        if self.ip_count == 0 or self.ip_count == self.max_count:
            self.getIPData()
            sleep(2)
            self.ip_count = 0
        return self.getProxy()


if __name__ == '__main__':
    p = ProxyMiddleware()
    proxy = p.getProxy()
    temp_url = "https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p5428.webp"
    res = requests.get(temp_url,proxies={'http':str(proxy)},headers = ua_headers)
    print(res.content)
