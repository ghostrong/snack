import sys
import BaseHTTPServer


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''Respond to HTTP requests with info about the request.'''

    # respond template
    page = '''
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>           </tr>
<tr>  <td>Datetime</td>       <td>{date_time}</td>   </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td> </tr>
<tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>     </tr>
<tr>  <td>Path</td>           <td>{path}</td>        </tr>
</table>
</body>
</html>
'''

    def do_GET(self):
        page = self._create_page()
        self._send_page(page)

    def _create_page(self):
        params = {
                'date_time': self.date_time_string(),
                'client_host': self.client_address[0],
                'client_port': self.client_address[1],
                'command': self.command,
                'path': self.path,
        }
        page = self.page.format(**params)
        return page

    def _send_page(self, page):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(page)))
        self.end_headers()
        self.wfile.write(page)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server_addr = ('', port)
    server = BaseHTTPServer.HTTPServer(server_addr, RequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
