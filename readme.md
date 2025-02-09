
# MANUAL DO UTILIZADOR

## 1. Introdução
Este manual tem como objetivo guiar o utilizador na instalação, configuração e utilização da ferramenta de segurança informática desenvolvida em Python. A aplicação permite realizar tarefas como:
- Ping
- Netdiscover
- Detetar e listar portas abertas em máquinas remotas
- Simular ataques de negação de serviço (DoS) com pacotes UDP
- Simular um ataque SYN Flood
- Analisar e processar arquivos de log de serviços como HTTP e SSH
- Troca de mensagens seguras entre cliente e servidor
- Port Knocking para acesso SSH

## 2. Requisitos de Sistema
A aplicação foi desenvolvida para ser executada em sistemas Linux e necessita de privilégios de root para funcionar corretamente. Certifique-se de que possui o Python instalado, bem como as bibliotecas e ferramentas necessárias.
Requisitos de Sistema:
- Sistema Operativo: Linux (ou variantes)
- Python 3.x
- Privilégios de Root (necessários para várias funcionalidades, como escaneamento de portas e execução de ataques)

## 3. Instalação de Dependências
Antes de utilizar a aplicação, é necessário instalar as bibliotecas Python e ferramentas externas que são necessárias para o funcionamento correto dos scripts.
- scapy: para análise de pacotes de rede.
- netifaces: para obter informações sobre as interfaces de rede.
- nmap: para escanear portas de rede.
- rsa: para criptografar e descriptografar mensagens.
- matplotlib: para gerar gráficos de estatísticas.
- requests: para interagir com APIs externas (caso necessário).

Comando:
```sh
pip install scapy netifaces nmap rsa matplotlib requests
```

## 4. Estrutura da Aplicação
A aplicação é composta por um conjunto de scripts Python, sendo o 

main.py

 o script principal. A partir deste, é possível acessar as funcionalidades da aplicação através de um menu interativo.
Estrutura de Diretórios:
```
/diretório_da_aplicação/
├── main.py                  # Menu principal que chama os outros scripts
├── ping.py                  # Script para fazer ping a um endereço IP
├── netdiscover.py           # Script para descobrir redes e dispositivos
├── port_scanner.py          # Script para escanear portas de rede
├── udp_flood.py             # Script para gerar UDP flood (ataque DoS)
├── tcp_flood.py             # Script para gerar SYN flood
├── log_files.py             # Script para analisar e processar logs
├── python_server.py         # Script para configurar o servidor de mensagens seguras
├── port_knocking.py         # Script para implementar port knocking para SSH
```

## 5. Como Utilizar a Aplicação
### Executando o Programa
1. Para executar o programa, abra o terminal e navegue até o diretório onde a aplicação está armazenada.
2. Execute o script principal com privilégios de root:

Comando:
```sh
sudo python3 main.py
```

## 6. Menu Principal
O 

main.py

 exibe um menu interativo que permite ao utilizador selecionar a ação desejada. As opções incluem:
- [1] Ping de um IP
- [2] Descoberta de Rede
- [3] Escanear Portas
- [4] UDP Flood (Ataque DoS)
- [5] SYN Flood (Ataque TCP SYN)
- [6] Análise de Logs
- [7] Troca de Mensagens Seguras (Servidor Python)
- [8] Port Knocking para SSH

## 7. Descrição das Funcionalidades
### 1. Ping de um IP
O script `ping.py` permite que o utilizador realize um ping a um endereço IP remoto, para verificar a conectividade com o servidor ou dispositivo.

### 2. Descoberta de Rede
O script `netdiscover.py` utiliza a biblioteca `scapy` para descobrir dispositivos e redes disponíveis na sua rede local.

### 3. Escanear Portas
Com o script `port_scanner.py`, o utilizador pode escanear portas abertas em uma ou mais máquinas remotas, utilizando a biblioteca `nmap`.

### 4. UDP Flood (Ataque DoS)
O script 

udp_flood.py

 gera um ataque de negação de serviço (DoS) com pacotes UDP, enviando tráfego para sobrecarregar a máquina de destino.

### 5. SYN Flood (Ataque TCP SYN)
O script 

tcp_flood.py

 executa um ataque SYN flood, utilizando pacotes TCP SYN para sobrecarregar um servidor e interromper os serviços de rede, como HTTP ou SMTP.

### 6. Análise de Logs
O script 

log_files.py

 processa os logs dos serviços instalados (por exemplo, HTTP e SSH), extraindo informações como tentativas de acesso inválidas, origem geográfica dos acessos e timestamps.

### 7. Troca de Mensagens Seguras
O script 

python_server.py

 implementa um sistema de troca de mensagens seguras entre um cliente e servidor, utilizando criptografia RSA (assimétrica).

### 8. Port Knocking para SSH
O script 

port_knocking.py

 implementa a técnica de port knocking para abrir temporariamente a porta SSH de uma máquina Linux. A técnica só permite o acesso SSH após um conjunto de "batidas" em portas específicas.
```

Salve este conteúdo no arquivo `README.md` no diretório `/home/kali/Desktop/lpd_trab/`.
Salve este conteúdo no arquivo `README.md` no diretório `/home/kali/Desktop/lpd_trab/`.