import BaseHTTPServer
import urlparse
import jinja2

with open('index.html', 'r') as f:
  index_page = f.read()
 

class HealthXHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    print parsed_path
    self.send_response(200)
    self.send_header('content-type', 'text/html')
    self.end_headers()

    template = jinja2.Template(index_page)
    self.wfile.write(template.render())

