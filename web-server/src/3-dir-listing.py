import os
import sys
import BaseHTTPServer


class ServerException(Exception):
    '''For internal error reporting'''
    pass


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''If the requested path maps to a file, that file is served.
    If is maps to a dir, then listing the dir.
    If anything goes wrong, an error page is constructed.
    '''

    error_page = '''
<html>
<body>
<h1>Error Accessing : {path}</h1>
<p>{msg}</p>
</body>
</html>
'''

    listing = '''
<html>
<body>
<ul>
{dirs}
</ul>
</body>
</html>
'''

    def do_GET(self):
        full_path = os.getcwd() + self.path
        try:
            if not os.path.exists(full_path):
                raise ServerException('"{}" not found'.format(self.path))
            elif os.path.isfile(full_path):
                self._handle_file(full_path)
            elif os.path.isdir(full_path):
                self._list_dir(full_path)
            else:
                raise ServerException('Unknown type: {}'.format(self.path))
        except ServerException as e:
            self._handle_error(e)

    def _handle_file(self, full_path):
        try:
            with open(full_path, 'r') as f:
                content = f.read()
        except IOError as e:
            msg = '"{}" cannot be read: {}'.format(self.path, e)
            self._handle_error(msg)
            return

        is_html = full_path.endswith('.html') or full_path.endswith('.htm')
        self._send_content(content, is_html)

    def _list_dir(self, full_path):
        try:
            entries = os.listdir(full_path)
        except IOError as e:
            msg = '"{}" cannot be listed: {}'.format(self.path, e)
            self._handle_error(msg)
            return

        dirs = '\n'.join(['<li>{}</li>'.format(d) for d in entries if not d.startswith('.')])
        page = self.listing.format(dirs=dirs)
        self._send_content(page)

    def _handle_error(self, msg):
        content = self.error_page.format(path=self.path, msg=msg)
        self._send_content(content)

    def _send_content(self, content, is_html=True):
        self.send_response(200)
        if is_html:
            self.send_header('Content-Type', 'text/html')
        else:
            self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server_addr = ('', port)
    server = BaseHTTPServer.HTTPServer(server_addr, RequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
