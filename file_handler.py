import os
import time
from mimetypes import guess_type

def check_file_access(file_path):
    """Check if file exists and is accessible"""
    if not os.path.exists(file_path):
        return 404
    if not os.access(file_path, os.R_OK):
        return 403
    return 200

def get_file_content(file_path):
    """Read file content with metadata"""
    with open(file_path, 'rb') as f:
        content = f.read()
    
    mime_type = guess_type(file_path)[0] or 'application/octet-stream'
    last_modified = time.strftime(
        '%a, %d %b %Y %H:%M:%S GMT',
        time.gmtime(os.path.getmtime(file_path))
    )
    
    return content, mime_type, last_modified