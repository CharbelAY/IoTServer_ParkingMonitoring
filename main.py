import time
from http.server import HTTPServer
from server import Server
from threading import Thread
import time
import db_connect as dbc 

#juliana

HOST_NAME = "localhost"
PORT_NUMBER = 8000

if __name__ == '__main__':
    h = HTTPServer((HOST_NAME,PORT_NUMBER),Server)
    print(time.asctime(), 'Server is up hosted %s:%s'%(HOST_NAME,PORT_NUMBER))
    try:
        t1 = Thread(target=h.serve_forever)
        t2 = Thread(target=dbc.Connect)
        t1.start()
        t2.start()
    except KeyboardInterrupt:
        h.server_close()
        print(time.asctime, "Server is shut down %s:%s"%(HOST_NAME,PORT_NUMBER))