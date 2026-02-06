import socket
import ssl

def run_secure_client():
    # 1. Konteks SSL Client
    context = ssl.create_default_context()

    # Karena self-signed certificate → verifikasi dimatikan
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # 2. Socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 3. Bungkus socket dengan SSL
    secure_sock = context.wrap_socket(sock, server_hostname='localhost')

    try:
        print("Menghubungkan ke Secure Server...")
        secure_sock.connect(('localhost', 10023))

        print(f"Terhubung dengan Cipher: {secure_sock.cipher()}")

        # Kirim pesan terenkripsi
        secure_sock.send(b"Halo, ini pesan rahasia CIA.")

        # Terima balasan
        response = secure_sock.recv(1024)
        print(f"Balasan Server: {response.decode()}")

    finally:
        secure_sock.close()

if __name__ == "__main__":
    run_secure_client()