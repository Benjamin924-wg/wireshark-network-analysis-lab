#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import struct
import zlib

def make_png(w=240, h=120):
    rows = b"".join(
        b"\x00" + bytes([30, 90, 130]) * w
        for _ in range(h)
    )

    def chunk(kind, data):
        body = struct.pack(">I", len(data)) + kind + data
        return body + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)

    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(rows))
        + chunk(b"IEND", b"")
    )

PNG = make_png()

PAGE = b"""<html>
<body>
<h2>Lab Login (HTTP - intentionally insecure)</h2>
<img src="/logo.png">
<form method="POST" action="/login">
User: <input name="username"><br>
Password: <input type="password" name="password"><br>
<input type="submit" value="Log in">
</form>
</body>
</html>"""

class H(BaseHTTPRequestHandler):
    def send_body(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/logo.png":
            self.send_body(200, "image/png", PNG)
        else:
            self.send_body(200, "text/html", PAGE)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        self.rfile.read(length)
        self.send_body(
            200,
            "text/html",
            b"<html><body>Login received (lab demo).</body></html>"
        )

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8081), H)
    print("Serving on http://127.0.0.1:8081 (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
