import socket
import select
import sys

def run_chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 9000))
    server_socket.listen(10)

    socket_list = [server_socket]
    clients = {}

    print("=== Select Server berjalan di port 9000 ===")

    while True:
        read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

        for sock in read_sockets:
            if sock == server_socket:
                client_socket, addr = server_socket.accept()
                socket_list.append(client_socket)
                clients[client_socket] = addr
                print(f"[BARU] Client {addr} bergabung")

            else:
                try:
                    data = sock.recv(1024)
                    if data:
                        pesan = f"[{clients[sock]}]: {data.decode()}\n"
                        for client_sock in socket_list:
                            if client_sock != server_socket and client_sock != sock:
                                client_sock.send(pesan.encode())
                    else:
                        socket_list.remove(sock)
                        print(f"[KELUAR] Client {clients[sock]} pergi")
                        sock.close()
                        del clients[sock]
                except:
                    socket_list.remove(sock)
                    sock.close()
                    continue

        for sock in exception_sockets:
            socket_list.remove(sock)
            sock.close()
            

if __name__ == "__main__":
    sys.exit(run_chat_server())