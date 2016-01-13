import vertx

client = vertx.create_http_client(port=8080, host="localhost")

def handle_body(body):
    print "Got data %s"% body

def handle_response(resp):
    print "Got response %s\n" % resp.status_code
    resp.body_handler(handle_body)

#get_now sends the simple get request without body immediately
#client.get_now("/file.txt", handle_response)
client.get_now("www.google.com", handle_response)
