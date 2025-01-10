#!/usr/share/python3
import socket, sys

#Conecta ao servidor do IANA
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org", 43))
#Envia o nome do dominio (ou IP) que desejamos coletar informações
s.send((sys.argv[1]+"\r\n").encode())
#Divide a string gerada e armazena a posição 19, onde é descrito a autoridade responsavel por aquele dominio
whois = s.recv(1024).split()
refer = whois[19]
#Fecha a conexão com a IANA
s.close()

#Agora vamos realizar a consulta nos conectando ao servidor da autoriadade responsavel

#Conecta ao servidor da autoridade responsavel
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((refer, 43))
#Envia o mesmo nome de dominio que passamos como arguramento
s1.send((sys.argv[1]+"\r\n").encode())
#Salva todas as informações coletadas na variavel result
result = s1.recv(1024)
print(result)

