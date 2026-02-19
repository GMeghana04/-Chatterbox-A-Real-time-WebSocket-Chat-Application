# -Chatterbox-A-Real-time-WebSocket-Chat-Application
Real-time chat application using WebSockets for persistent, bi-directional communication. FastAPI backend manages concurrent client connections, instantly broadcasting messages to all participants. Creates a dynamic shared chat room where users communicate in real-time with automatic message delivery and online presence tracking.
# 💬 REAL-TIME CHATTERBOX APPLICATION

A modern, real-time chat application built with **FastAPI** (WebSockets) and a clean **HTML/CSS/JavaScript** frontend. This application features secure user authentication, persistent chat history, and a responsive, interactive user interface with real-time messaging capabilities.

![Chatterbox Demo](https://via.placeholder.com/800x400?text=Chatterbox+Live+Demo)

## 🚀 Features

- **Real-Time Messaging**: Instant message delivery using WebSocket full-duplex communication
- **Persistent Chat History**: Messages stored in SQLite database and retrieved upon login
- **Secure Authentication**: Password hashing with Bcrypt and session management via UUID tokens
- **Online Users List**: Real-time tracking of active users in the chat room
- **Responsive UI**: Mobile-friendly design with messages styled differently for sender/receiver
- **Session Persistence**: LocalStorage integration to keep users logged in across browser refreshes
- **Message Formatting**: Timestamps and user identification for all messages
- **Auto-Reconnection**: Automatic WebSocket reconnection on connection loss

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.9+)
- **Database**: SQLite with SQLite3
- **WebSocket**: FastAPI WebSocket support
- **Authentication**: Bcrypt for password hashing, UUID for session tokens
- **Server**: Uvicorn (ASGI server)

### Frontend
- **HTML5**: Semantic markup for chat interface
- **CSS3**: Flexbox layout, gradients, animations, responsive design
- **JavaScript**: Vanilla JS with WebSocket client
- **LocalStorage**: Session persistence

## 📂 Project Structure
REAL-TIME-CHATTER-APPLICATION/
├── server/ # Backend FastAPI application
│ ├── auth.py # Authentication routes (register/login)
│ ├── config.py # Configuration settings
│ ├── database.py # Database initialization and operations
│ ├── models.py # Pydantic models for request/response
│ ├── server.py # Main FastAPI app with WebSocket endpoint
│ ├── websocket_manager.py # WebSocket connection manager
│ ├── requirements.txt # Backend dependencies
│ └── chat.db # SQLite database file
│
├── client/ # Python client (optional)
│ ├── client.py # Terminal-based chat client
│ └── requirements.txt # Client dependencies
│
├── frontend/ # Web frontend
│ └── index.html # Single-page application with:
│ ├── Login/Register UI # Tabbed authentication forms
│ ├── Chat Interface # Real-time messaging layout
│ ├── Online Users Sidebar # Active users list
│ └── Embedded CSS/JavaScript # Styling and WebSocket logic
│
├── .gitignore # Git ignore rules
├── LICENSE # MIT License
└── README.md # Project documentation

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge)

### Step 1: Clone the Repository
```bash
git clone https://github.com/GMeghana04/-Chatterbox-A-Real-time-WebSocket-Chat-Application.git
cd -Chatterbox-A-Real-time-WebSocket-Chat-Application

Step 2: Set Up Backend
# Navigate to server directory
cd server

# Install dependencies
pip install fastapi uvicorn websockets bcrypt python-multipart

# Or install from requirements.txt
pip install -r requirements.txt

Step 3: Run the Server
bash
# Start the FastAPI server
cd server
uvicorn server:app --reload  
Expected output:
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.

Step 4: Access the Application
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
🎮 Usage Guide
1. Registration
Click on the "Register" tab

Enter a username and password

Click Register button

Success message will appear

2. Login
Switch to "Login" tab

Enter your credentials

Click Login button

You'll be automatically redirected to chat

3. Chat Interface
Your messages: Appear on the right side with gradient background

Others' messages: Appear on the left side with white background

Online users: Shown in the left sidebar with live count

System messages: Centered in blue (join/leave notifications)

4. Sending Messages
Type your message in the input box

Press Enter or click the send button (➤)

Messages appear instantly for all users

5. Logout
Click the "Logout" button in the top-right corner

You'll be redirected to the login screen

🔄 Real-Time Features
Feature	Description
WebSocket Connection	Persistent bi-directional communication
Live User Updates	Online users list updates in real-time
Instant Messaging	Messages appear without page refresh
Connection Status	Visual indicator showing connected/disconnected state
Auto-Reconnect	Automatically reconnects if connection drops
🔒 Security Implementation
Password Security: All passwords hashed using Bcrypt before storage

Session Management: UUID v4 tokens for authenticated sessions

Token Validation: WebSocket connections validate tokens before allowing access

No Plain Text: Passwords never stored or transmitted in plain text

Input Validation: Server-side validation for all user inputs

📊 Database Schema
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
🌐 API Endpoints
Endpoint	Method	Description
/	GET	API status check
/register	POST	Register new user
/login	POST	Login and get token
/ws?token={token}	WebSocket	Real-time chat connection
🧪 Testing with Multiple Users
To test real-time features:

Open the app in different browsers (Chrome, Firefox, Edge)

Or use Incognito/Private windows

Register/Login with different usernames

Start chatting between windows to see real-time updates

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👩‍💻 Author
GMeghana04

GitHub: @GMeghana04

Project Link: https://github.com/GMeghana04/-Chatterbox-A-Real-time-WebSocket-Chat-Application

🙏 Acknowledgments
FastAPI for the amazing WebSocket support

Bcrypt for secure password hashing

All contributors and users of this project

📸 Screenshots
Add screenshots of your application here

Login Screen	Chat Interface
https://via.placeholder.com/300x200	https://via.placeholder.com/300x200
🚧 Future Enhancements
User profile pictures

Private messaging

Message reactions

File sharing

Voice/Video calls

End-to-end encryption

Mobile app (React Native)

