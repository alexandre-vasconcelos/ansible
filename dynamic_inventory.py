#!/usr/bin/env python3
import json
import subprocess
import ipaddress

# Substitua a faixa de IP pela sua rede
network_range = '10.0.0.0/24'
active_hosts = []

# Usando a biblioteca ipaddress para iterar sobre os endereços IP
network = ipaddress.IPv4Network(network_range)

# Adiciona uma mensagem de depuração para indicar que o script foi iniciado
print("Iniciando o processo de verificação de hosts ativos...")

# Loop sobre todos os endereços IP na rede
for ip in network.hosts():
    ip = str(ip)

    # Adiciona uma mensagem para indicar qual IP está sendo verificado
    print(f"Verificando IP: {ip}")

    response = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Verifica se o comando ping teve sucesso
    if response.returncode == 0:  # Se o host responder ao ping
        print(f"Host ativo encontrado: {ip}")
        active_hosts.append(ip)
    else:
        print(f"Host {ip} não respondeu ao ping.")

# Criar o formato de inventário em JSON
inventory = {
    "all": {
        "hosts": active_hosts
    }
}

# Exibe a saída em formato JSON
print("Inventário de hosts ativos:")
print(json.dumps(inventory, indent=4))
