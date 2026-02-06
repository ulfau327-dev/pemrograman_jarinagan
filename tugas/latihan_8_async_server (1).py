import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[BARU] Koneksi dari {addr}")

    try:
        while True:
            # Baca data dari client (non-blocking)
            data = await reader.read(100)
            if not data:
                print(f"[PUTUS] {addr} menutup koneksi.")
                break

            message = data.decode().strip()
            print(f"[{addr}] Mengirim: {message}")

            # Balas client
            response = f"Echo: {message}\n"
            writer.write(response.encode())
            await writer.drain()  # Pastikan buffer terkirim

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"=== Async Server Berjalan di {addrs} ===")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer Dimatikan.")