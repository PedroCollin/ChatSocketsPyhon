import socket, threading

def handle_messages(connection: socket.socket):


    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Erro ao enviar a msg ao servidor: {e}')
            connection.close()
            break

def client() -> None:

    SERVER_ADDRESS = '10.122.15.214'
    SERVER_PORT = 12005

    try:

        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        print('Connectado ao chat!')


        while True:
            msg = input()

            if msg == 'sair':
                break


            socket_instance.send(msg.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Erro ao conectar ao servidor {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()