import urllib2
import re

site = input("Enter URL : ")

for page in range(1,5):
    req = urllib2.Request(site + str(100) + str(page) + ".html")
    resp = urllib2.urlopen(req)
    respData = resp.read()
    paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

    for eachP in paragraphs:
        print(site + str(100) + str(page) + ".html" + " : " + eachP)

resp.close()
