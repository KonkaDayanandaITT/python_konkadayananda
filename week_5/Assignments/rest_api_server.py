import http.server
import socketserver
import json

PORT = 8001

books = {}
next_id = 1
class MyHandler(http.server.BaseHTTPRequestHandler):
    
    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def do_GET(self):
        parts = self.path.strip("/").split("/")

        if len(parts) == 1 and parts[0] == "books":
            self._send_response(200, list(books.values()))

        elif len(parts) == 2 and parts[0] == "books":
            try:
                book_id = int(parts[1])
                if book_id in books:
                    self._send_response(200, books[book_id])
                else:    
                    self._send_response(404, {"error": "Book not found"})
            except:
                self._send_response(400, {"error": "Invalid Id"})
        else:
            self._send_response(404, {"error": "Not Found"})

    def do_POST(self):
        global next_id
        
        if self.path == "/books":
            content_len = int(self.headers.get("content-length",0))
            body = self.rfile.read(content_len)
            data = json.loads(body)
            
            data["id"] = next_id
            books[next_id] = data
            next_id += 1
            
            self._send_response(201, data)
        else:
            self._send_response(404, {"error": "Not found"})
            
    def do_PUT(self):
        parts = self.path.strip("/").split("/")

        if len(parts) == 2 and parts[0] == "books":
            try:
                book_id = int(parts[1])
                
                if book_id not in books:
                    self._send_response(404, {"error":"Book not found"})
                    return

                content_len = int(self.headers.get("content-length", 0))
                body = self.rfile.read(content_len)
                new_data = json.loads(body)
                
                books[book_id].update(new_data)
                self._send_response(200, books[book_id])

            except:
                self._send_response(400, {"error": "Invalid Id"})
        else:
            self._send_response(404, {"error": "Not Found"})
            
    def do_DELETE(self):
        parts = self.path.strip("/").split("/")

        if len(parts) == 2 and parts[0] == "books":
            try:
                book_id = int(parts[1])

                if book_id in books:
                    del books[book_id]
                    self._send_response(200, {"message": "Book deleted"})
                    return
                else:
                    self._send_response(404, {"error": "Book not found"})
            except:
                self._send_response(400, {"error": "Invalid Id"})
        else:
            self._send_response(404, {"error": "Not Found"})
            
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()