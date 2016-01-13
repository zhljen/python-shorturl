import vertx
from shorturl import ShortenURL

server = vertx.create_http_server()

@server.request_handler
def request_handler(request):
    print request.method
    print request.uri
    if ( request.method == 'GET' ):
        short_url = ShortenURL().shorten(request.uri)
    request.response.end(short_url)
      
server.listen(8080)
