import asyncio
import websockets
import json

DATABASE = "database.json"

async def handler(websocket):
    print("Client WS terhubung")
    while True:
        try:
            with open(DATABASE) as f:
                data = json.load(f)
            if data:
                await websocket.send(json.dumps(data[-1]))
            await asyncio.sleep(2)
        except:
            break

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server aktif di port 8765")
        await asyncio.Future()

asyncio.run(main())