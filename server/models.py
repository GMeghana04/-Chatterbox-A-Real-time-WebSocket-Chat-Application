from pydantic import BaseModel


# -------------------------------
# User Registration Model
# -------------------------------
class UserRegister(BaseModel):
    username: str
    password: str


# -------------------------------
# User Login Model
# -------------------------------
class UserLogin(BaseModel):
    username: str
    password: str


# -------------------------------
# Message Model (Optional)
# -------------------------------
class ChatMessage(BaseModel):
    sender: str
    message: str
    timestamp: str

