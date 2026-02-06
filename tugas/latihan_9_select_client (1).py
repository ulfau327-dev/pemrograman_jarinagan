import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Server menutup koneksi.")
                break
            print(data.decode().strip())
        except:
            break

def main():
    host = '127.0.0.1'
    port = 9000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Terkoneksi ke server {host}:{port}")

    # Thread untuk menerima pesan
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == 'bye':
            break
        client_socket.send(msg.encode())

    client_socket.close()
    print("Koneksi ditutup.")

if __name__ == "__main__":
    main()