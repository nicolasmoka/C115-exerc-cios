from socket import *

serverName = 'localhost'
serverPort = 3000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Número de questões
qtdQuestoes = int(clientSocket.recv(1024).decode('utf-8'))

for _ in range(qtdQuestoes):
    pergunta = clientSocket.recv(1024).decode('utf-8')
    print(pergunta)
    resposta = input("Escreva sua resposta: ").strip()
    clientSocket.sendall(resposta.encode('utf-8'))

resultado = clientSocket.recv(1024).decode('utf-8')
print("\nResultado:")
print(resultado)

clientSocket.close()
