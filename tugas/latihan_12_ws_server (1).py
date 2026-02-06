import asyncio
import websockets
import json
import random

# Menyimpan semua client yang terhubung
CONNECTED_CLIENTS = set()

async def stock_handler(websocket):
    """Handler dijalankan tiap client connect"""
    print("[NEW] Client bergabung.")
    CONNECTED_CLIENTS.add(websocket)

    try:
        # Kirim pesan selamat datang
        await websocket.send(json.dumps({"msg": "Welcome to Stock Ticker!"}))

        # Loop untuk mendengarkan pesan client
        async for message in websocket:
            print(f"Client sent: {message}")

    except websockets.exceptions.ConnectionClosed:
        print("[CLOSED] Client terputus.")
    finally:
        CONNECTED_CLIENTS.remove(websocket)

async def broadcast_price():
    """Generate harga palsu dan broadcast tiap detik"""
    while True:
        price_data = {
            "symbol": "BBCA",
            "price": random.randint(8000, 8500),
            "timestamp": "Live"
        }
        message = json.dumps(price_data)

        if CONNECTED_CLIENTS:
            websockets.broadcast(CONNECTED_CLIENTS, message)
            print(f"[BROADCAST] {message} -> ke {len(CONNECTED_CLIENTS)} clients")

        await asyncio.sleep(1) # update tiap detik

async def main():
    async with websockets.serve(stock_handler, "localhost", 6789):
        print("=== WebSocket Server running on ws://localhost:6789 ===")
        await broadcast_price()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server Stopped.")