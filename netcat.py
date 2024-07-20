import socket
import sys

def main(ip, port):
    try:
        # Cria um socket TCP/IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Conecta ao servidor
            s.connect((ip, int(port)))
            
            # Recebe a resposta do servidor
            data = s.recv(1024).decode('utf-8').strip()
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")
        return

    # Exibe o resultado obtido
    print(data)

print("\x1bc\x1b[47;34m")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python cliente.py <IP> <PORTA>")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]

    main(ip, port)


    

