import BaseHTTPServer
import healthX

if __name__ == '__main__':
  server = BaseHTTPServer.HTTPServer(('127.0.0.1', 8080), healthX.HealthXHandler)
  print 'Running the server...'
  server.serve_forever()
  print 'Done.'
