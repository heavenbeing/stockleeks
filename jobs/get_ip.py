import requests  # requests模块需要使用 pip 命令安装

headers = {
    'cache-control': 'no-cache',
}

response = requests.get('http://ip.cip.cc')

print('ip address:')
print(response.text)

