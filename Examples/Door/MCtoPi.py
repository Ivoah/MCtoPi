from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer



class MCtoPi(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.get(self.wfile, self.path.strip('/'))

def start(Handler, port = 3141):
    server = HTTPServer(('', port), Handler)
    server.serve_forever()

if __name__ == '__main__':
    class Handler(MCtoPi):
        def get(self, output, input):
            print(input)
            output.write(input)

    print 'Serving on port 3141'
    try:
        start(Handler, 3141)
    except KeyboardInterrupt:
        pass
    print('\nBye!')
