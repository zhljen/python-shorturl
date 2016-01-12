import vertx

server = vertx.create_http_server()

@server.request_handler
def request_handler(request):
    print request.method
    print request.uri
    if ( request.method == 'GET' ):
        file = 'index.html'
    elif '..' not in request.path:
        file = request.path
    request.response.send_file(file) 
      
server.listen(8080)
