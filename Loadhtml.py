import urllib2
import sys
import re
import urllib
from bs4 import BeautifulSoup

if __name__ == '__main__':
	req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
             'Accept':'text/html;q=0.9,*/*;q=0.8',
             'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
             'Accept-Encoding':'gzip',
             'Connection':'close',
             'Referer':None 
             }
	url = sys.argv[1]
	Key_Words = sys.argv[2]
	req_timeout = 5
	req = urllib2.Request(url,None,req_header)
	resp = urllib2.urlopen(req,None,req_timeout)
	soup = BeautifulSoup(resp,"html.parser")
	Title = soup.title.get_text()
	Context = soup.p.get_text()
	print Title
	for con in soup.find_all('p'):
		context = con.get_text()
		Is_In = re.compile(r'([\s\S]*)%s([\s\S]*)'%(Key_Words),re.S)
		matchObj = Is_In.search(context)
		if matchObj:
			print context

	
