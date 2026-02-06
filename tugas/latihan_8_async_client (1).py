import asyncio

async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print("Terkoneksi ke server!")

    try:
        while True:
            msg = input("Ketik pesan (atau 'bye' untuk keluar): ")
            if msg.lower() == 'bye':
                print("Menutup koneksi...")
                break

            # Kirim pesan ke server
            writer.write(msg.encode())
            await writer.drain()

            # Tunggu balasan server
            data = await reader.read(100)
            print(f"Server: {data.decode().strip()}")

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(tcp_client())