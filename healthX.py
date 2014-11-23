import BaseHTTPServer
import urlparse

class HealthXHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    print parsed_path
    self.send_response(200)
    self.send_header('content-type', 'text/html')
    self.end_headers()
    self.wfile.write('Shit')

