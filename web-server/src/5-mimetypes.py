import os
import sys
import mimetypes
import getopt
import BaseHTTPServer


class ServerException(Exception):
    '''For internal error reporting'''
    pass


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''If the requested path maps to a file, that file is served.
    If is maps to a dir, then listing the dir.
    If anything goes wrong, an error page is constructed.
    '''

    ERR_NOT_PERM = 403
    ERR_NOT_FOUND = 404
    ERR_INTERNAL = 500

    FILE_TYPES = mimetypes.types_map

    debug_mode = False

    root_directory = None

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
        full_path = self._get_abs_path()
        self._log('Access to the path: {}'.format(full_path))

        if not full_path.startswith(self.root_directory):
            self._log('Not belong to the root_directory !')
            msg = 'Path "{}" not below root "{}"'.format(full_path, self.root_directory)
            self._err_not_perm(msg)

        elif not os.path.exists(full_path):
            self._log('Not exist: {}'.format(full_path))
            self._err_not_found(full_path)

        elif os.path.isfile(full_path):
            self._log('"{}" is a file.'.format(full_path))
            self._handle_file(full_path)

        elif os.path.isdir(full_path):
            self._log('"{}" is a directory.'.format(full_path))
            self._list_dir(full_path)

        else:
            self._log('Cannot tell what it is !')
            self._err_internal('Cannot tell: {}'.format(full_path))

    def _get_abs_path(self):
        return os.path.normpath(os.getcwd() + self.path)

    def _handle_executable(self, full_path, query_params):

    def _handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as f:
                content = f.read()
        except IOError as e:
            msg = '"{}" cannot be read: {}'.format(self.path, e)
            self._err_not_perm(msg)
            return

        file_type = self._guess_file_type(full_path)
        self._send_content(content, file_type)

    def _guess_file_type(self, full_path):
        base, ext = os.path.splitext(full_path)
        ext = ext.lower()
        return self.FILE_TYPES.get(ext, 'application/octet-stream')

    def _list_dir(self, full_path):
        try:
            entries = os.listdir(full_path)
        except IOError as e:
            msg = '"{}" cannot be listed: {}'.format(self.path, e)
            self._err_not_perm(msg)
            return

        dirs = '\n'.join(['<li>{}</li>'.format(d) for d in entries if not d.startswith('.')])
        page = self.listing.format(dirs=dirs)
        self._send_content(page)

    def _send_content(self, content, file_type='text/html'):
        length = str(len(content))
        self._log('Sending content, File-Type: {}, Length: {}'.format(file_type, length))
        self.send_response(200)
        self.send_header('Content-Type', file_type)
        self.send_header('Content-Length', length)
        self.end_headers()
        self.wfile.write(content)

    def _err_internal(self, msg):
        self.send_error(self.ERR_INTERNAL, msg)

    def _err_not_found(self, msg):
        self.send_error(self.ERR_NOT_FOUND, msg)

    def _err_not_perm(self, msg):
        self.send_error(self.ERR_NOT_PERM, msg)

    def _log(self, msg):
        if self.debug:
            print 'Logging:', msg


def usage():
    msg = 'Usage:\n-p: port \n-d: root_directory \n-v: debug(0 or 1)'
    print msg


def main():
    options, rest = getopt.getopt(sys.argv[1:], 'd:p:v:')
    if len(options) != 3:
        usage()
        return

    for flag, arg in options:
        if flag == '-p':
            port = int(arg)
        elif flag == '-d':
            RequestHandler.root_directory = os.path.abspath(arg)
        elif flag == '-v':
            RequestHandler.debug = bool(int(arg))

    server_addr = ('', port)
    server = BaseHTTPServer.HTTPServer(server_addr, RequestHandler)

    print 'Serving at: {}:{}'.format(*server_addr)
    print 'Root path is:', RequestHandler.root_directory
    server.serve_forever()


if __name__ == '__main__':
    main()
