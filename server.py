import socket
from datetime import datetime

# Configurações do servidor
HOST = '0.0.0.0'  # Endereço IP do servidor (0.0.0.0 para escutar em todas as interfaces)
PORT = 8080       # Porta que o servidor irá escutar
print("\x1bc\x1b[47;34m")
# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do socket do servidor ao endereço e porta especificados
server_socket.bind((HOST, PORT))

# Coloca o servidor em modo de escuta, com um backlog de 5 conexões
server_socket.listen(5)

print(f"Servidor ouvindo na porta {PORT}...")

try:
    while True:
        # Aguarda por uma nova conexão de um cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")

        # Obtém a data e hora atuais
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Envia a data e hora atuais para o cliente
        client_socket.sendall(current_datetime.encode('utf-8'))

        # Fecha a conexão com o cliente
        client_socket.close()
except KeyboardInterrupt:
    print("\nServidor interrompido pelo usuário.")

# Fecha o socket do servidor
server_socket.close()

