import os
import time

def setup_www_directory():
    """Initialize the web root directory"""
    if not os.path.exists('www'):
        os.makedirs('www')
    
    # Create default index file if none exists
    index_path = os.path.join('www', 'index.html')
    if not os.path.exists(index_path):
        with open(index_path, 'w') as f:
            f.write("""<!DOCTYPE html>
<html>
<head><title>Python Web Server</title></head>
<body>
<h1>Welcome to Python Web Server</h1>
<p>Default index page</p>
</body>
</html>""")

def parse_headers(header_lines):
    """Parse HTTP headers into a dictionary"""
    headers = {}
    for line in header_lines:
        if line:
            key, value = line.split(':', 1)
            headers[key.lower().strip()] = value.strip()
    return headers

def create_response(status_code, status_text, headers=None):
    """Create an HTTP response"""
    if headers is None:
        headers = {}
    
    # Ensure Connection: close is always included unless overridden
    if 'Connection' not in headers:
        headers['Connection'] = 'close'
    
    status_line = f"HTTP/1.1 {status_code} {status_text}\r\n"
    header_lines = ""
    for key, value in headers.items():
        header_lines += f"{key}: {value}\r\n"
    
    return status_line + header_lines + "\r\n"

def log_request(client_ip, path, status_code):
    """Log requests to server.log"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    log_entry = f"{timestamp} - {client_ip} - {path} - {status_code}\n"
    with open('server.log', 'a') as f:
        f.write(log_entry)
