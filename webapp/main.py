from fastapi import FastAPI, WebSocket, WebSocketDisconnect


app = FastAPI()

class ConnectionManager:
    def __init__(self):
        pass
        self.active_connections = []
        self.usernames = {}
 
    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.usernames[websocket] = username
        await self.broadcast(f"{username} joined the chat")
 
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        username = self.usernames.pop(websocket, "unknown user")
        return username
 
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
 
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"{username}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        username = manager.disconnect(websocket)
        await manager.broadcast(f"{username} left the chat")    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)