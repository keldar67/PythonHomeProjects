import traceback
from bs4 import BeautifulSoup
import requests
from PodcastScraper import PodcastScraper
links = []
links.append('https://www.podbean.com/podcast-detail/hqwed-393e3/THE-ADAM-BUXTON-PODCAST')
links.append('https://www.podbean.com/podcast-detail/bdn39-2f011/No+Such+Thing+As+A+Fish')
links.append('https://www.podbean.com/podcast-detail/mheih-63aa8/The-A-to-Z-of-David-Bowie-Podcast')
links.append('https://www.podbean.com/podcast-detail/ge4iy-3620a/Friday+Night+Comedy+from+BBC+Radio+4')
links.append('https://www.podbean.com/podcast-detail/wmn2j-2f257/The-Infinite-Monkey-Cage-Podcast')

links.append('https://www.podbean.com/podcast-detail/p63ta-5b555/The-Jim-Jefferies-Show-Podcast')
links.append('https://www.podbean.com/podcast-detail/pje5k-74621/Drunk-Women-Solving-Crime-Podcast')
#links.append('')

#links.append('')
page_link = links[0]


page_response = requests.get(page_link, timeout = 5)
page_content = BeautifulSoup(page_response.content, 'html.parser')

episodelinks = []
scrapers = []

try:
    tablebody = page_content.find('tbody',{'class':'items'})

    for tr in tablebody.find_all('tr'):

        #Grab the Title of the Podcast
        thedata = tr.find_all('td')[1]
        theTitle = thedata.find_all('a', {'class':'title listen-now'})[0].text
        theDate = thedata.find_all('span', {'class':'datetime'})[0].text
        d = theDate.split('-')
        theDate = '-'.join([d[2],d[1],d[0]])

        #print(theTitle, theDate)

        #Grab the cell from each row at position 4 (index 3)
        thedata = tr.find_all('td')[3]

        #The link should be the only one in there (index 0)
        thelink = thedata.find_all('a', {'class':'download'})[0]

        downloadlink = 'https://www.podbean.com' + thelink.attrs['href']

        # Create a PodcastScraper object for the new entry
        x = PodcastScraper(theTitle, theDate, downloadlink, 'ADAM BUXTON')

        # And add it to the list of scraper objects
        scrapers.append(x)

        #Append the link    
        episodelinks.append(downloadlink)

        #episode_page = requests.get(episodelinks[0])
        
    #for alink in episodelinks: print(alink)
    for pcs in scrapers: print(pcs)
    
except AttributeError as error:
    print ('Error finding table in link: ' + page_link)
    print(''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__)))
