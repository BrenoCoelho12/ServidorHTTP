# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: Edson Breno Coelho Neves e Rony de Sena Lourenço
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket
import os

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    # imprime na tela o que o cliente enviou ao servidor
    print (request.decode('utf-8'))
    # declaracao da resposta do servidor
    request = request.decode('utf-8').split(" ") #divide a string a partir do espaço
    print(request)

    if request[0] == "GET": #se a primeira string for get

        path = request[1]
        if not os.path.exists(path): #caso o caminho não exista não exista
            print("O arquivo não foi encontrado.")
            arquivo = open("erro404.html", encoding ="utf-8").read() #abre arquivo e ler
            http_response = """\
    HTTP/1.1 404 Not Found\r\n\r\n
    """ + arquivo

        else: #caso o arquivo exista
            arquivo = open("index.html", encoding = "utf-8").read() #abre arquivo e ler
            http_response = """\
        HTTP/1.1 200 OK
        """ + arquivo

    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send(http_response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()
