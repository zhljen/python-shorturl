
import redis

REDIS_HOSTNAME = 'localhost'
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ShortenURL(object):
    """
     the request -- hit_counter -- ( hit_counter, longURL ), ( shortURL, hit_counter )
    """
    def __init__(self):
        self.domain = 'http://myshorten/'
        self.redis_server = redis.Redis(REDIS_HOSTNAME)
        self.redis_server.set('hit_counter', 0)

    def shorten(self, longURL):
        res = self.redis_server.get(longURL)
        if res != None:
            return res

        curid = self.redis_server.incr('hit_counter');
        shorturl = self.domain + self.encode(curid)

        self.redis_server.set(shorturl, longURL)
        return shorturl

    def redirect(self, url):
        print "redirect to ", url
        return url

    def encode(self, integer):
        if integer == 0:
            return '0'

        string = ""
        while integer > 0:
            remainder = integer % BASE
            string = ALPHABET[remainder] + string
            integer /= BASE
        return string

if __name__ == '__main__':
    testURL1="www.yahoo.com"
    testURL2="www.cnn.com"
    a = ShortenURL()
    #a=Api(login="pythonbitly",apikey="R_06871db6b7fd31a4242709acaf1b6648")
    shortres=a.shorten(testURL1)
    print "Short URL = %s" % shortres
    short=a.shorten(shortres)
    print "Short URL = %s" % short
    short=a.shorten(testURL1)
    print "Short URL with history = %s" % short
    # urlList=[testURL1,testURL2]
    # shortList=a.shorten(urlList)
    # print "Short URL list = %s" % shortList
    # long=a.expand(short)
    # print "Expanded URL = %s" % long
    # info=a.info(short)
    # print "Info: %s" % info
    # stats=a.stats(short)
    # print "User clicks %s, total clicks: %s" % (stats.user_clicks,stats.total_clicks)
    # errors=a.errors()
    # print "Errors: %s" % errors
    # testURL3=["www.google.com"]
    # short=a.shorten(testURL3)
    # print "Short url in list = %s" % short