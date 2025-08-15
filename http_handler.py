import os
import time
from mimetypes import guess_type
from file_handler import get_file_content, check_file_access
from utils import create_response, parse_headers, log_request

def handle_client(client_socket, client_address):
    """Handle a single client connection"""
    try:
        # Receive raw bytes
        raw_request = client_socket.recv(1024)
        # Attempt to decode as UTF-8, handle errors
        try:
            request = raw_request.decode('utf-8')
        except UnicodeDecodeError:
            # If decoding fails, return 400 Bad Request
            response = create_response(400, "Bad Request")
            client_socket.sendall(response.encode('utf-8'))
            return

        if not request:
            return
            
        # Parse request
        lines = request.split('\r\n')
        request_line = lines[0]
        parts = request_line.split()
        
        if len(parts) < 2:
            response = create_response(400, "Bad Request")
            client_socket.sendall(response.encode())
            return
            
        method, path = parts[0], parts[1]
        headers = parse_headers(lines[1:])
        
        # Process request
        if method in ('GET', 'HEAD'):
            response = process_http_request(method, path, headers)
        else:
            response = create_response(405, "Method Not Allowed")
        
        # Send response
        if isinstance(response, str):
            response = response.encode('utf-8')
        client_socket.sendall(response)
        
        # Log request
        status_code = int(response.split(b' ')[1])
        log_request(client_address[0], path, status_code)
        
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        client_socket.close()

def process_http_request(method, path, headers):
    if path == '/':
        path = '/index.html'
    
    file_path = os.path.join('www', path.lstrip('/'))
    
    # Check file access
    access_status = check_file_access(file_path)
    if access_status != 200:
        if access_status == 404:
            return create_response(404, "File Not Found")
        elif access_status == 403:
            return create_response(403, "Forbidden")  # Return immediately
        else:
            return create_response(access_status, "Unknown Error")
    
    # Check conditional headers
    if 'if-modified-since' in headers:
        if not is_modified_since(file_path, headers['if-modified-since']):
            return create_response(304, "Not Modified")
    
    # Get file content
    content, mime_type, last_modified = get_file_content(file_path)
    
    # Check supported MIME types
    supported_mime_types = [
        'text/html', 'text/plain',
        'image/jpeg', 'image/png'
    ]
    if mime_type not in supported_mime_types:
        return create_response(415, "Unsupported Media Type")
    
    # Build response
    response_headers = {
        'Content-Type': mime_type,
        'Content-Length': len(content),
        'Last-Modified': last_modified,
        'Connection': headers.get('connection', 'close')
    }
    
    response = create_response(200, "OK", response_headers)
    
    if method == 'GET':
        if isinstance(response, str):
            response = response.encode('utf-8') + content
        else:
            response += content
    
    return response

def is_modified_since(file_path, if_modified_since):
    """Check If-Modified-Since header"""
    try:
        # Get file modification time in UTC and round to nearest second
        file_time = round(os.path.getmtime(file_path))
        
        # Parse If-Modified-Since header (in GMT/UTC)
        struct_time = time.strptime(if_modified_since, '%a, %d %b %Y %H:%M:%S GMT')
        # Convert to UTC timestamp (time.mktime assumes local time, so adjust for UTC)
        header_time = int(time.mktime(struct_time) - time.timezone)
        
        # Compare timestamps
        return file_time > header_time
    except Exception as e:
        print(f"Error parsing If-Modified-Since: {e}")
        return True

