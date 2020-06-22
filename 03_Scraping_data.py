import requests  # allows us to download html
from bs4 import BeautifulSoup  # allows us to use html data, grab it,scrap it
import pprint #to print things nicely

res = requests.get('https://news.ycombinator.com/')  # get request to get this page (info)
res2= requests.get('https://news.ycombinator.com/news?p=2')
#print(res.text)  # entire html file
#clean up data with BeautifulSoup
soup=BeautifulSoup(res.text,'html.parser') #from string to object
soup2=BeautifulSoup(res2.text,'html.parser')
#print(soup.body.contents)
#print(soup.find_all('div')) #'a':to find all the links
#print(soup.a) #firts a tag that comes up, also  ### find()
links=soup.select('.storylink') #is going to grab all the scores on the page .:is for class
links2=soup2.select('.storylink')
#print(soup.select('#score_22844788')) #: is for id
votes=soup.select('.score')
votes2=soup2.select('.score')
#print(votes[0].get('id')) #vrne nam id od score prvega elementa iz spletne strani
#print(links[0].getText())
#print(votes[0].getText())
links_new=links+links2
votes_new=votes+votes2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['Score'], reverse=True) #od največjega do najmanjšega
#vse naslove damo v nov seznam
def create_custom_hn(links,votes):
	hn=[]
	for idx, item in enumerate(links):
		title=links[idx].getText() #lahko zamenjamo z item.getText()
		href=links[idx].get('href', None) #None in case if href not working/not correct
    #Težava: Če 1 naslov nima nobenin points
		points=int(votes[idx].getText().replace(' points',''))
		#if points>100:
		hn.append({'title':title,'link': href, 'Score': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links_new,votes_new))


	