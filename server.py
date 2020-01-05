from http.server import BaseHTTPRequestHandler
from routes import routes
from pathlib import Path
import db_connect as dbc
import utilities as ut



class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        return self.respond()

    def handle_http(self):
        status=200
        content_type = "application/json"
        # response_content=""

        result = dbc.getStatus()
        # result = ut.prepare_html(result[0]["status"])

        if self.path in routes:
            # print(routes[self.path])
            route_content=routes[self.path]["template"]
            filepath=Path("templates/{}".format(route_content))
            if (filepath.is_file()):
                # content_type = "application/json"
                #response_content = open("templates/{}".format(route_content))
                #response_content = response_content.read()
                response_content=result
            else:
                # content_type = "text/plain"
                response_content = "404 Not Found"
        else:
            # content_type = "text/plain"
            response_content = "404 Not Found"
        
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        response_content=bytes(str(response_content), "UTF-8")
        return response_content

    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)