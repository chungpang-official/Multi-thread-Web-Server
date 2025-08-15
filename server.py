import os
import socket
import threading
from http_handler import handle_client
from file_handler import get_file_content
from utils import setup_www_directory

def start_server(host='127.0.0.1', port=8080):
    """Main server entry point"""
    setup_www_directory()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server running on {host}:{port}")
        print(f"Serving files from: {os.path.abspath('www')}")
        
        while True:
            client_socket, addr = server_socket.accept()
            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, addr)
            )
            thread.daemon = True
            thread.start()
            
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()
