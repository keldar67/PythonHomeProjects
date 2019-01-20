from bs4 import BeautifulSoup

class PodcastScraper:
    """
    Podcast
    """

    #-------------------
    # Members
    #-------------------
    title = ''
    date = ''
    downloadpagelink = ''
    downloadlink = ''

    #-------------------
    # Methods
    #-------------------
    def __init__(self, title, date, downloadpagelink):
        self.title = title
        self.date = date
        self.downloadpagelink = downloadpagelink

    def __str__(self):
        return self.date + ' - ' + self.title + ' - ' + self.downloadpagelink

    def GetDownloadLink():
        pass

    def DownloadLink():
        pass
    
