#!/usr/bin/python python      
import requests
from bs4 import BeautifulSoup
        
def getTarget():
	print "[+]Enter the url:"
	url = raw_input()
	print "[+]Checking URL"
	global req
	req = requests.get(url)
	checkUrl(req)
	print "[+]Crawling.."
	url = req.text
	soup = BeautifulSoup(url, 'html.parser')
	#print soup
	links = []
	imgs = []
	print "\n"
	print "[+]Links Found:"
	for link in soup.find_all('a'):
		try:
			links.append(link.get('href'))
			links.remove("#")
			links.remove('None')
		except:
			a=5
	links = set(links)
	for l in links:
		print l
	
	print "\n"
	print "[+]Images Found:"
	for img in soup.find_all('img'):
		try:
			imgs.append(img.get('src'))
		except:
			a=5
	imgs = set(imgs)
	for i in imgs:
		print i

def checkUrl(req):
	if(req.status_code==requests.codes.ok):
        	print "[+]URL: 200 OK"


if __name__ == "__main__":
    getTarget() #Get the url
