import json

with open('data.json', encoding='utf-8') as f:
    qiita_data = json.load(f)
    title = qiita_data[0]['titles']
    urls = qiita_data[0]['urls']
    #print(title)
    #print(urls)

for title,url in zip(title,urls):
    print(title, url)