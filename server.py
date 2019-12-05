from http.server import BaseHTTPRequestHandler
from routes import routes
from pathlib import Path
import db_connect as dbc

#thank you for you charboul aka ba2dounis

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        return self.respond()

    def handle_http(self):
        status=200
        content_type = "text/plain"
        response_content=""

        dbc.getStatus()

        if self.path in routes:
            print(routes[self.path])
            route_content=routes[self.path]["template"]
            filepath=Path("templates/{}".format(route_content))
            if (filepath.is_file()):
                content_type = "text/html"
                response_content = open("templates/{}".format(route_content))
                response_content = response_content.read()
            else:
                content_type = "text/plain"
                response_content = "404 Not Found"
        else:
            content_type = "text/plain"
            response_content = "404 Not Found"
        
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(response_content, "UTF-8")

    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)