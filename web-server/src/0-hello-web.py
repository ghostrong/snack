import sys
import BaseHTTPServer


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning fixed content.'''

    content = 'Hello World!'

    # Handle a GET request
    # HTTP headers: http://en.wikipedia.org/wiki/List_of_HTTP_header_fields
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', str(len(self.content)))
        self.end_headers()
        self.wfile.write(self.content)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server_addr = ('', port)
    server = BaseHTTPServer.HTTPServer(server_addr, RequestHandler)

    print 'Serving at {0}:{1}'.format(*server_addr)
    server.serve_forever()


if __name__ == '__main__':
    main()
