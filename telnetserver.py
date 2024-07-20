import socket

def start_telnet_server(host, port):
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Faz bind do socket ao endereço e porta especificados
    server_socket.bind((host, port))
    
    # Coloca o socket em modo de escuta
    server_socket.listen(1)
    print(f"Servidor Telnet ouvindo em {host}:{port}...")

    # Aguarda por uma conexão
    client_socket, client_address = server_socket.accept()
    print(f"Conexão recebida de {client_address}")

    with client_socket:
        while True:
            # Recebe a mensagem do cliente
            client_message = client_socket.recv(1024).decode('utf-8').strip()
            if not client_message:
                print("Cliente enviou uma mensagem em branco. Conexão encerrada.")
                break
            
            print(f"Mensagem recebida do cliente: {client_message}")

            # Lê a mensagem de resposta do usuário do servidor
            server_message = input("Digite a mensagem para enviar ao cliente: ").strip()
            if not server_message:
                print("Mensagem em branco. Conexão encerrada.")
                break

            # Envia a mensagem de volta ao cliente
            client_socket.sendall(server_message.encode('utf-8'))

    # Fecha o socket do servidor
    server_socket.close()
print("\x1bc\x1b[47;34m")
if __name__ == '__main__':
    HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede
    PORT = 8080       # Porta para escutar
while True:
    start_telnet_server(HOST, PORT)

