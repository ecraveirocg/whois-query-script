**Whois Query Script**
Este script automatiza o processo de consulta WHOIS para um domínio, realizando duas consultas sucessivas a servidores WHOIS para obter informações detalhadas sobre o domínio ou endereço IP.

>Descrição

O script utiliza o protocolo WHOIS para consultar informações sobre um domínio. Ele realiza as seguintes etapas:

- Conecta-se ao servidor principal da IANA (Internet Assigned Numbers Authority) para realizar a consulta inicial.
- Obtém o servidor de referência (um servidor WHOIS específico para o domínio) a partir da resposta do servidor IANA.
- Conecta-se ao servidor de referência para obter informações adicionais sobre o domínio e imprime os resultados.

>Funcionalidade

O script realiza as seguintes operações:

- Conexão TCP com o servidor whois.iana.org na porta 43.
- Envio do domínio (ou IP) passado como argumento via linha de comando.
- Processamento da resposta para encontrar o servidor WHOIS de referência.
- Conexão com o servidor WHOIS de referência para coletar informações adicionais.
- Exibição das informações coletadas.
