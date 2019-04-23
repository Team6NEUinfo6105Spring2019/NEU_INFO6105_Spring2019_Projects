import requests,re
import pandas as pd
import time

def getURL(pageNum):
    url = 'https://jobs.bnymellon.com/jobs?page='
    urlback = '&categories=Global%20Markets'
    urls = 
    for i in range(pageNum):
        temp = url+(str)(i+1)+urlback
        urls.append(temp)
    print(urls)
    return urls

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('404 error!')
        return(' ')

def fillPositionList(html):
    time.sleep(2)
    pattern = re.compile('"canonical_url":"(.*?)"')
    p = re.findall(pattern, html)
    if p:
        p_de = sorted(set(p),key=p.index)
        return p
    return 'N'

def printCsv(sinfo):
    df = pd.DataFrame(sinfo)
    df.to_csv('/Users/jinyimu/Documents/INFO6105/GLJob.csv', sep=',', header=True, index=True) # set output path

def main():
    sinfo = 
    urls = getURL(2) # set the number of page you want
    i = 1
    for url in urls:
        html = getHTMLText(url)
        sinfo.extend(fillPositionList(html))
        if i % 5 == 0:
            print("%d / %d" %(i,len(urls)))
        i += 1
    printCsv(sinfo)
    print('working')

main()


