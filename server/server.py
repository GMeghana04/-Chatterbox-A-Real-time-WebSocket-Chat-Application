from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import config
from websocket_manager import ConnectionManager
from auth import router
from database import init_db, save_message, get_chat_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()
init_db()
app.include_router(router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    if token not in config.sessions:
        await websocket.close(code=1008)
        return

    username = config.sessions[token]
    await manager.connect(username, websocket)
    
    try:
        await asyncio.sleep(0.1) # Stabilization delay
        await manager.broadcast_user_list()
        
        # Load History
        history = get_chat_history()
        for msg in history:
            try:
                formatted_history = f"[{msg['timestamp']}] {msg['username']}: {msg['message']}"
                await websocket.send_text(formatted_history)
            except Exception as e:
                print(f"Error sending history item: {e}")

        await manager.broadcast_message("Server", f"{username} joined the chat!")

        while True:
            data = await websocket.receive_text()
            if data.strip():
                save_message(username, data)
                await manager.broadcast_message(username, data)

    except WebSocketDisconnect:
        print(f"ℹ️ {username} disconnected.")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")
    finally:
        manager.disconnect(username)
        try:
            await manager.broadcast_message("Server", f"{username} left the chat!")
            await manager.broadcast_user_list()
        except:
            pass