import http.server
import socketserver
import json
import os

PORT = 3000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/photos':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            images_dir = 'images'
            if not os.path.exists(images_dir):
                self.wfile.write(json.dumps([]).encode('utf-8'))
                return
            
            files = os.listdir(images_dir)
            image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif'))]
            
            photos = []
            thumbs = {f for f in image_files if '_thumb' in f}
            fulls = {f for f in image_files if '_full' in f}
            
            processed = set()
            for f in image_files:
                # If it's a thumb, it'll be handled with its _full counterpart, or we can just skip it here
                if f in processed or f in thumbs:
                    continue
                
                if f in fulls:
                    prefix = f.replace('_full', '')
                    thumb = next((t for t in thumbs if t.startswith(prefix)), f)
                    photos.append({
                        'full': f'images/{f}',
                        'thumb': f'images/{thumb}'
                    })
                    processed.add(f)
                else:
                    # Normal standalone image without _full or _thumb naming
                    photos.append({
                        'full': f'images/{f}',
                        'thumb': f'images/{f}'
                    })
                    processed.add(f)
                    
            self.wfile.write(json.dumps(photos).encode('utf-8'))
        else:
            return super().do_GET()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
