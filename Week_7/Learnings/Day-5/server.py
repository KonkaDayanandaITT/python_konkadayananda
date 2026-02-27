from http.server import BaseHTTPRequestHandler, HTTPServer
import json

books = [
    {"id": 1, "title": "Book A"},
    {"id": 2, "title": "Book B"}
]

class BookHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/books":
            response_body = json.dumps(books)
            response_bytes = response_body.encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response_bytes)))
            self.end_headers()

            self.wfile.write(response_bytes)

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/books":

            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)

            try:
                data = json.loads(body.decode())

                new_id = len(books) + 1
                new_book = {
                    "id": new_id,
                    "title": data.get("title"),
                    "author": data.get("author"),
                    "year": data.get("year")
                }

                books.append(new_book)

                response_body = json.dumps(new_book)
                response_bytes = response_body.encode()

                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response_bytes)))
                self.end_headers()

                self.wfile.write(response_bytes)

            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("127.0.0.1", 8080), BookHandler)

print("Server running at http://127.0.0.1:8080")
server.serve_forever()