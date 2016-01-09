import urllib.request
import re
URL='http://www.qiushibaike.com/text'
HEADERS={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
RE=r'<div class="content">(?P<content>.*?)<!--'
# 远程增加一行文字
class Spider(object):
    def __init__(self):
        '''
            初始化一个实例,该实例的xiaohualist属性就是我们想要的结果
        '''
        self.pattern=re.compile(RE,re.S)
        page=self._getpage()
        self._analyzepage(page)

    def refresh(self):
        page=self._getpage()
        self._analyzepage(page)

    def _getpage(self):
        request=urllib.request.Request(URL,headers=HEADERS)
        return urllib.request.urlopen(request).read().decode()

    def _analyzepage(self,page):
        self.xiaohualist=[]
        list=self.pattern.finditer(page)
        for content in list:
            self.xiaohualist.append(content.group('content'))
