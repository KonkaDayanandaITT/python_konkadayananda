from http.server import BaseHTTPRequestHandler, HTTPServer
import json

books = [
    {"id" :1, "title" : "Book A"},
    {"id" :2, "title" : "Book B"}
]

class BookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/books":
            response_body = json.dumps(books)
            
            self.send_response(200)
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()
            
            self.wfile.write(response_body.encode())
            
        else:
            self.send_response(404)
            self.end_headers()
            
server = HTTPServer(("127.0.0.1", 8080), BookHandler)
        
print("Server running at http://127.0.0.1:8080")
server.serve_forever() 