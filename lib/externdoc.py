import urllib2
import re
import hashlib
import datetime

from os import path, makedirs
from urllib import urlretrieve

from BeautifulSoup import BeautifulSoup

class ExternalDoc:
    def __init__(self, link):
        self.conn = self._connect(link)
        self.soup = BeautifulSoup(self.conn.read(), smartQuotesTo=None)
        self.pic_paths = {}
        
    def _connect(self, link):
        try:
            content = urllib2.urlopen(link)
        except urllib2.HTTPError as eHTTP:
            print "HTTP error {0}, {1}".format(eHTTP.errno, eHTTP.strerror)
        except urllib2.URLError as eURL:
            print "URL not accessible {0}, {1}".format(eURL.errno, eURL.strerror)
        except:
            raise     
        return content
    
    def parseHTML(self):
        # replace remote url with local url
        exturls = self.soup('a')
        for index, url in enumerate(exturls):
            matches = re.compile(r"^(.*\/)([^\s]+)\.(jpg|png|gif|bmp)$", re.I).match(url['img'])
            hashgen = hashlib.md5()
            hashgen.update(matches.group(2))
            hashgen.update(str(index))
            
            today = datetime.date.today()
            picpath = "../static/img_store_root/" + str(today.year) + "-" + str(today.month) + "/"
            if path.exists(picpath) == False:
                makedirs(picpath)
                
            hashgen.update(str(datetime.datetime.now()))
            picpath += hashgen.hexdigest()
            
            ## they are different
            if self.pic_paths[picpath] == None:
                self.pic_paths[picpath] = self.soup('a')[index]['href']
            else:
                print "Hash conflicts"
                raise
            self.soup('a')[index]['href'] = picpath
            
            for path in self.pic_paths:
                urlretrieve(self.pic_paths[path], path)
    
            return self.soup.prettify()