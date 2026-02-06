import socket

# 1. Membuat socket TCP (IPv4)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind ke alamat dan port
server.bind(('localhost', 12345))

# 3. Listen (maksimal 1 antrian client)
server.listen(1)
print("Server siap... menunggu client")

# 4. Accept koneksi (BLOCKING)
conn, addr = server.accept()
print("Client terhubung dari:", addr)

# 5. Terima pesan dari client
data = conn.recv(1024).decode('utf-8')
print("Pesan dari client:", data)

# 6. Kirim balasan ke client
conn.send("Halo Client, pesanmu diterima".encode('utf-8'))

# 7. Tutup koneksi
conn.close()
server.close()
print("Server selesai")