#百度翻译爬取
import requests
words=input('请输入你要翻译的内容:')
data= {
    'from': 'zh',
    'to': 'en',
    'query': words,
    'transtype': 'translang',
    'simple_means_flag': '3'      #百度神坑啊
}
#由于百度的限制,需要加一个头部信息,来伪装成用浏览器访问的
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
        }

url='https://fanyi.baidu.com/basetrans'

# 将网址,请求包,以及头部信息传入requests模块,并以post请求方式发送请求.
result=requests.post(url,data=data,headers=headers)
# 粗暴的打印全部结果
print(result.text)

#根据我的试验以及前面暗示的flag,
# 发现,百度翻译在翻译时将翻译分为两种,
# 一种是单词翻译(长度<=3),另一种是句子翻译(长度>3)
#这两种不同的翻译方式,返回的结果有着很大的不同,如下:
if len(words)<=3:
    l=list(result.json()['dict']['word_means'])
    #由于单词一般都有好几个意思,打印出来是个列表,不太美观,利用循环挨个打印出来.
    for i in l:
        print(i)
else:
    print(result.json()['trans'][0]['dst'])
