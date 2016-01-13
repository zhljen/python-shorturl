
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)

class URLStore(object):
    def __init__(self):
        self.domain = 'http://myshorten/'
        self.urls = {}

    def set(self, key, value):
        self.urls[key] = value
        return value

    def get(self, key):
        if key in self.urls:
            return self.urls[key]
        return None

class ShortenURL(object):
    """
     the request -- hit_counter -- ( hit_counter, longURL ), ( shortURL, hit_counter )
    """
    def __init__(self):
        self.domain = 'http://myshorten/'
        self.store = URLStore()
        self.store.set('hit_counter', 0)

    def shorten(self, uri):
        res = self.store.get(uri)
        if res != None:
            return res

        curid = self.store.set('hit_counter', self.store.get('hit_counter') + 1 );

        shorturl = self.domain + self.encode(curid)

        self.store.set(shorturl, uri)
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

