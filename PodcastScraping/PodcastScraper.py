from bs4 import BeautifulSoup
import os

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
    savefolder = ''

    #-------------------
    # Methods
    #-------------------
    def get_download_path():
        """
        Returns the default downloads path for linux or windows
        taken from:
        https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
        """
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')


        
    def __init__(self, title, date, downloadpagelink, downloadpath):
            self.title = title
            self.date = date
            self.downloadpagelink = downloadpagelink
            self.downloadpath = downloadpath
            self.savefolder = str(get_download_path()) + '\\POD\\' + self.downloadpath
            print(self.savefolder)

            
    def __str__(self):
        return self.date + ' - ' + self.title + ' - ' + self.downloadpagelink

    def GetDownloadLink():
        pass

    def DownloadLink():
        pass

    

        
