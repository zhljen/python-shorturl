import vertx
from core.streams import Pump

server = vertx.create_net_server()

@server.connect_handler
def connect_handler(socket):
    Pump(socket, socket).start()

server.listen(1234)