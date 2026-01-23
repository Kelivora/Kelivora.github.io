#!/usr/bin/env python3
"""
Quick server starter for port 2527
Usage: python3 start_server.py [port]
Default port: 2527
"""

import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 2527
DIR = sys.argv[2] if len(sys.argv) > 2 else '.'

os.chdir(DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[Server] {self.address_string()} - {format % args}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Server running at http://localhost:{PORT}")
    print(f"📂 Serving directory: {os.path.abspath(DIR)}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
