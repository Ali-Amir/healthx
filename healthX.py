import BaseHTTPServer
import urlparse

class HealthXHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
