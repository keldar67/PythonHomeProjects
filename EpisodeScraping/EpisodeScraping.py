


from bs4 import BeautifulSoup
import requests

def GetSoup(theURL):
	page_contents = BeautifulSoup(requests.get(theURL, timeout = 5)"html.parser")


myURL = 
