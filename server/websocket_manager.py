from fastapi import WebSocket
from typing import Dict
from datetime import datetime


class ConnectionManager:
    def __init__(self):
        # username -> websocket
        self.active_connections: Dict[str, WebSocket] = {}

    # -------------------------------
    # Connect User
    # -------------------------------
    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[username] = websocket

    # -------------------------------
    # Disconnect User
    # -------------------------------
    def disconnect(self, username: str):
        if username in self.active_connections:
            del self.active_connections[username]

    # -------------------------------
    # Get Online Users
    # -------------------------------
    def get_online_users(self):
        return list(self.active_connections.keys())

    # -------------------------------
    # Broadcast Chat Message
    # -------------------------------
    async def broadcast_message(self, sender: str, message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")
        disconnected_users = []

        for username, connection in self.active_connections.items():
            try:
                if username == sender:
                    formatted = f"[{timestamp}] Me: {message}"
                else:
                    formatted = f"[{timestamp}] {sender}: {message}"

                await connection.send_text(formatted)

            except:
                # Mark broken connections
                disconnected_users.append(username)

        # Clean up disconnected users
        for user in disconnected_users:
            self.disconnect(user)

    # -------------------------------
    # Broadcast Online Users List
    # -------------------------------
    async def broadcast_user_list(self):

        users = ", ".join(self.get_online_users())
        message = f"🟢 Online Users: {users}"

        disconnected_users = []

        for username, connection in self.active_connections.items():
            try:
                await connection.send_text(message)
            except:
                disconnected_users.append(username)

        for user in disconnected_users:
            self.disconnect(user)
