#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import urllib.request
import urllib.error
from pathlib import Path

PORT = 8080
DIRECTORY = Path(__file__).parent
API_BASE = 'https://signal.coze.com'
API_KEY = 'agent-world-cd5516f477f1ac4dfcd5c1219c3485d050f4e9a006af8647'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def do_GET(self):
        if self.path.startswith('/api/'):
            self.proxy_api()
            return
        if self.path == '/' or self.path == '/index.html':
            self.path = '/dashboard.html'
        return super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api/'):
            self.proxy_api()
            return

    def do_OPTIONS(self):
        self.send_response(200)
        self.add_cors_headers()
        self.end_headers()

    def add_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, agent-auth-api-key')

    def proxy_api(self):
        url = API_BASE + self.path
        body = None
        if self.command == 'POST':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)

        headers = {
            'agent-auth-api-key': API_KEY,
            'Content-Type': 'application/json',
        }

        req = urllib.request.Request(url, data=body, headers=headers, method=self.command)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.add_cors_headers()
                self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
                self.send_header('Content-Length', len(data))
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.add_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(e.read())
        except urllib.error.URLError as e:
            self.send_response(502)
            self.add_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e.reason)}).encode())

    def end_headers(self):
        self.add_cors_headers()
        super().end_headers()

def main():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║            策场Signal Arena 交易可视化面板                    ║
║══════════════════════════════════════════════════════════════║
║  服务器地址: http://localhost:{PORT}                           ║
║  API代理:    {API_BASE}                                       ║
║  按 Ctrl+C 停止服务器                                        ║
╚══════════════════════════════════════════════════════════════╝
    """)

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")

if __name__ == "__main__":
    main()
