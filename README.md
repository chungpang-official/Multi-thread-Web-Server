Python Web Server Project
Overview
This project implements a multi-threaded HTTP/1.1 web server in Python for the Comp 2322 Computer Networking course. The server handles HTTP GET and HEAD requests, supports various status codes (200, 304, 400, 404, 415), implements conditional requests using Last-Modified and If-Modified-Since headers, and manages persistent (Connection: keep-alive) and non-persistent (Connection: close) connections. It also logs all requests to a file.
Note: The 403 Forbidden status could not be tested on Apollo due to system restrictions enforcing rw permissions for the owner. The implementation is correct but was limited by the environment.
Requirements

Python: Version 3.6 or higher
Dependencies: None (uses only Python standard library)

Directory Structure

www/: Web root directory containing files to be served (e.g., index.html, test.jpg, test.pdf).
server.py: Main server script that sets up the socket and handles multi-threading.
file_handler.py: Module for file access, content retrieval, and MIME type handling.
http_handler.py: Module for parsing HTTP requests and generating responses.
utils.py: Helper functions for logging and default content generation.
server.log: Log file recording all requests (timestamp, client IP, requested file, status code).

How to Run

Ensure Python 3.6+ is installed:python3 --version


Place files to serve in the www/ directory (e.g., index.html).
Run the server:python3 server.py


Access the server at http://127.0.0.1:8080/ using a browser or tools like curl:curl http://127.0.0.1:8080/index.html



Features

HTTP Methods: Supports GET and HEAD requests.
Status Codes:
200 OK: Successful requests.
304 Not Modified: For conditional requests.
400 Bad Request: For invalid requests.
404 Not Found: For non-existent files.
415 Unsupported Media Type: For unsupported file types (e.g., PDFs).
403 Forbidden: Implemented but untestable on Apollo due to permission restrictions.


Conditional Requests: Handles Last-Modified and If-Modified-Since headers.
Connection Handling: Supports Connection: keep-alive for persistent connections and Connection: close for non-persistent connections.
Logging: Logs all requests to server.log in the format: YYYY-MM-DD HH:MM:SS - IP - /path - STATUS.

Notes

Default Port: The server runs on port 8080.
Log Persistence: The log file (server.log) is appended to, not overwritten, across server restarts.
Testing Environment: Tested on Apollo, a university-managed server. The 403 Forbidden status could not be triggered due to system policies enforcing rw permissions for the owner. All other functionalities were fully tested and work as expected.

Limitations

Due to Apollo’s permission restrictions, the 403 Forbidden status could not be tested. The implementation checks for read access using os.access(), but the system prevented setting permissions to deny read access.

Author

[Leung Chung Pang]
Student ID: [23093488d]
Course: Comp 2322 Computer Networking
Submission Date: April 30, 2025

