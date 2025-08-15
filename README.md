# 🐍 Python Web Server Project

## 📖 Overview
This project implements a **multi-threaded HTTP/1.1 web server in Python** for the *Comp 2322 Computer Networking* course.  

Key capabilities:  
- Handles **HTTP GET** and **HEAD** requests.  
- Supports status codes: **200**, **304**, **400**, **404**, **415**.  
- Implements conditional requests via **Last-Modified** and **If-Modified-Since** headers.  
- Manages **persistent** (`Connection: keep-alive`) and **non-persistent** (`Connection: close`) connections.  
- Logs all requests to a file.  

> **Note:**  
> The `403 Forbidden` status could not be tested on *Apollo* due to system restrictions enforcing read/write permissions for the owner. The implementation is correct but environment-limited.

---

## 📦 Requirements
- **Python**: Version `3.6+`  
- **Dependencies**: None (uses only Python standard library)  

---

## 📂 Directory Structure
```
www/             # Web root directory with served files (e.g., index.html, test.jpg, test.pdf)
server.py        # Main server script (socket setup + multi-threading)
file_handler.py  # File access, content retrieval, MIME type handling
http_handler.py  # HTTP request parsing & response generation
utils.py         # Helper functions for logging & default content generation
server.log       # Log file: YYYY-MM-DD HH:MM:SS - IP - /path - STATUS
```

---

## 🚀 How to Run

1. **Verify Python version**:
   ```bash
   python3 --version
   ```

2. **Place files** to serve in the `www/` directory (e.g., `index.html`).  

3. **Run the server**:
   ```bash
   python3 server.py
   ```

4. **Access the server**:  
   - Browser: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)  
   - Or with `curl`:
     ```bash
     curl http://127.0.0.1:8080/index.html
     ```

---

## ✨ Features

### 🔹 HTTP Methods
- **GET**
- **HEAD**

### 🔹 Status Codes
| Code | Description | Notes |
|------|-------------|-------|
| `200 OK` | Successful requests | — |
| `304 Not Modified` | Conditional requests | — |
| `400 Bad Request` | Invalid requests | — |
| `404 Not Found` | File does not exist | — |
| `415 Unsupported Media Type` | Unsupported file types (e.g., PDF) | — |
| `403 Forbidden` | Implemented, untestable on Apollo | Env. restriction |

### 🔹 Conditional Requests
- Implements **Last-Modified** and **If-Modified-Since** headers.

### 🔹 Connection Handling
- Supports `Connection: keep-alive`  
- Supports `Connection: close`

### 🔹 Logging
- All requests logged in `server.log`:
  ```
  YYYY-MM-DD HH:MM:SS - IP - /path - STATUS
  ```

---

## 🗒 Notes
- **Default Port**: `8080`  
- **Log Persistence**: `server.log` is appended to (not overwritten) across restarts.  
- **Testing Environment**:  
  - Tested on **Apollo** (university-managed server).  
  - `403 Forbidden` could not be triggered due to enforced read/write permissions.  
  - All other functions fully tested and working.

---

## ⚠️ Limitations
- `403 Forbidden` untestable in Apollo due to system restrictions.  
- Implementation checks read access with `os.access()`, but permission denial simulation not possible in this environment.

---

## 👤 Author
- **Name**: Leung Chung Pang  
- **Student ID**: 23093488d  
- **Course**: Comp 2322 Computer Networking  
- **Submission Date**: *April 30, 2025*
