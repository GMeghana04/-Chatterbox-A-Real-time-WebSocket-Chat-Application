🚀 ChatterBox – Real-Time WebSocket Chat Application
📌 Overview

ChatterBox is a full-stack real-time chat application built using FastAPI and WebSockets.
It enables secure user authentication, instant bi-directional communication, automated content moderation, and an admin monitoring dashboard.

This project demonstrates:
Modern backend architecture
JWT-based authentication
Role-based authorization
Real-time communication handling
Database-driven message persistence

### ✨ Key Features

🔐 User Registration & Login
Secure user account creation
Credential validation during login
🎫 JWT-Based Authentication
Token generated upon successful login
Stateless session management
Token validation before WebSocket access
🔑 Secure Password Hashing (bcrypt)
Passwords stored in hashed format
Protection against plain-text password storage
👤 Authenticated User Identity Management
Username extracted from JWT
Message ownership clearly identified
💬 Real-Time Messaging using WebSockets
Persistent bi-directional communication
Instant message broadcasting
No polling required
📡 Multi-User Concurrent Support
Handles multiple connected users simultaneously
Asynchronous backend architecture
🔁 Live Message Broadcasting
Messages sent by one user delivered to all active users
Event-driven architecture
🗄️ SQLite Database Integration
Stores registered users
Stores chat history persistently
🕒 Message Timestamping
Each message tagged with time
Improves message traceability
📜 Chat History Retrieval
Previously stored messages available
Persistent conversation storage
🧠 Connection Manager Module
Tracks active WebSocket connections
Handles connect & disconnect events
🎨 Structured Frontend Interface
Separate Login & Chat pages
Clean and minimal UI design
➡️ Message Differentiation UI
Current user messages aligned right
Other users’ messages aligned left
🔄 Auto Scroll for New Messages
Automatically scrolls to latest message
🛡️ Access-Controlled WebSocket Endpoint
Only authenticated users can join chat
Prevents anonymous access
📂 Modular Project Structure
Backend and frontend separated
Clean file organization
🧪 Error Handling & Connection Handling
Handles invalid tokens
Handles disconnections gracefully
🌐 Local Deployment Ready
Runs on Uvicorn server
Frontend accessible via browser
📦 Version Control with Git & GitHub
MIT Licensed
Open-source ready

### 🛠️ Tech Stack
### 🔹 Backend
FastAPI
SQLAlchemy
SQLite
Python-Jose (JWT Authentication)
Passlib (bcrypt hashing)
WebSockets
Uvicorn

### 🔹 Frontend
HTML5
CSS3
JavaScript
Fetch API

### 📂 Project Structure
### 📂 **server/** - Backend Application
- `auth.py` - User registration and login
- `config.py` - Configuration settings
- `database.py` - Database operations
- `models.py` - Data models
- `server.py` - Main FastAPI server
- `websocket_manager.py` - WebSocket connections
- `requirements.txt` - Python dependencies
- `chat.db` - SQLite database

### 📂 **client/** - Python Client (Optional)
- `client.py` - Terminal-based chat client
- `requirements.txt` - Client dependencies

### 📂 **frontend/** - Web Interface
- `index.html` - Complete chat application with:
  - Login/Register UI
  - Real-time chat interface
  - Online users sidebar
  - Embedded CSS styling
  - JavaScript WebSocket logic

### 📄 **Root Directory Files**
- `.gitignore` - Git ignore rules
- `LICENSE` - MIT License
- `README.md` - Project documentation
  
## ⚙️ Installation & Setup
### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge)

### Step 1: Clone the Repository
git clone https://github.com/GMeghana04/-Chatterbox-A-Real-time-WebSocket-Chat-Application.git
cd -Chatterbox-A-Real-time-WebSocket-Chat-Application

### Step 2: Set Up Backend
# Navigate to server directory
cd server

# Install dependencies
pip install fastapi uvicorn websockets bcrypt python-multipart

# Or install from requirements.txt
pip install -r requirements.txt

### Step 3: Run the Server
# Start the FastAPI server
cd server
uvicorn server:app --reload  
Expected output:
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.

### Step 4: Access the Application
Open your browser and navigate to:
http://127.0.0.1:8000
Note: The root endpoint shows API status
Open the frontend directly:
Navigate to the frontend folder
Open index.html in your browser
Or use a simple HTTP server:
cd frontend
python -m http.server 5500
Then visit: http://127.0.0.1:5500

### 🎮 Usage Guide
### 1. Registration
Click on the "Register" tab
Enter a username and password
Click Register button
Success message will appear

### 2. Login
Switch to "Login" tab
Enter your credentials
Click Login button
You'll be automatically redirected to chat

### 3. Chat Interface
Your messages: Appear on the right side with gradient background
Others' messages: Appear on the left side with white background
Online users: Shown in the left sidebar with live count
System messages: Centered in blue (join/leave notifications)

### 4. Sending Messages
Type your message in the input box
Press Enter or click the send button (➤)
Messages appear instantly for all users

### 5. Logout
Click the "Logout" button in the top-right corner
You'll be redirected to the login screen

### 🔄 Real-Time Features
Feature	Description
WebSocket Connection : Persistent bi-directional communication
Live User Updates : Online users list updates in real-time
Instant Messaging : Messages appear without page refresh
Connection Status : Visual indicator showing connected/disconnected state
Auto-Reconnect : Automatically reconnects if connection drops

### 🔒 Security Implementation
Password Security: All passwords hashed using Bcrypt before storage
Session Management: UUID v4 tokens for authenticated sessions
Token Validation: WebSocket connections validate tokens before allowing access
No Plain Text: Passwords never stored or transmitted in plain text
Input Validation: Server-side validation for all user inputs

### 📊 Database Schema
Users Table
sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
Messages Table
sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL
);

### 🌐 API Endpoints
Endpoint	Method	Description
/	GET	API status check
/register	POST	Register new user
/login	POST	Login and get token
/ws?token={token}	WebSocket	Real-time chat connection

### 🧪 Testing with Multiple Users
To test real-time features:
Open the app in different browsers (Chrome, Firefox, Edge)
Or use Incognito/Private windows
Register/Login with different usernames
Start chatting between windows to see real-time updates

### 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

### 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

### 🚧 Future Enhancements
User profile pictures
Private messaging
Message reactions
File sharing
Voice/Video calls
End-to-end encryption
Mobile app (React Native)

