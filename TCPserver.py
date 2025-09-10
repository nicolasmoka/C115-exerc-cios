from socket import *
import json

with open('Questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

serverPort=3000
serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = conexão TCP
serverSocket.bind(('', serverPort)) # atribui a porta ao socket criado
# aceita conexões com no máximo 1 cliente na fila
serverSocket.listen(1)
print('O servidor está pronto para receber')

connectionSocket,addr=serverSocket.accept()

# enviando a quantidade de questões
connectionSocket.sendall(str(len(questions)).encode('utf-8'))

# enviando perguntas
for q in questions:
    texto = f'\n\n{q["question"]}\n' + '\n'.join([op for op in q["options"]]) + '\n'
    connectionSocket.sendall(texto.encode('utf-8'))
    response=connectionSocket.recv(1024).decode('utf-8').strip()
    q['client_answer']=response

# vendo quais perguntas o usuário acertou
hits=0
feedback=[]
for q in questions:
    correct=q['answer']==q['client_answer']
    feedback.append(f"{'\u2714\uFE0F ' if correct else '\u274C'} {q['question']}")
    if correct:
        hits += 1

# enviando resultado
result = f"Nota: {hits}/{len(questions)}\n" + "\n".join(feedback)
connectionSocket.sendall(result.encode('utf-8'))

# encerrando conexão
connectionSocket.close()
serverSocket.close()
