import scapy.all as scapy
import socket

# Função para escanear a rede e encontrar dispositivos
def scan(ip):
    # Cria uma requisição ARP para os dispositivos na rede
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # Envia o pacote e recebe a resposta
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Lista de dispositivos encontrados
    devices_list = []
    for element in answered_list:
        device = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device)
    return devices_list

# Função para gerar o arquivo HTML com os resultados
def generate_html(devices):
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dispositivos Conectados à Rede</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f4f4f9;
            }
            h1 {
                text-align: center;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: #fff;
                padding: 8px;
                margin: 5px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h1>Dispositivos Conectados à Rede Local</h1>
        <ul>
    """
    
    # Adiciona dispositivos encontrados à lista HTML
    for device in devices:
        html_content += f'<li>IP: {device["ip"]} - MAC: {device["mac"]}</li>'
    
    # Fecha o HTML
    html_content += """
        </ul>
    </body>
    </html>
    """

    # Salva o arquivo HTML
    with open("dispositivos_rede.html", "w") as file:
        file.write(html_content)
    print("Arquivo HTML gerado com sucesso: dispositivos_rede.html")

# Função principal
def main():
    # Define a faixa de IP a ser escaneada (exemplo para uma rede local típica 192.168.1.1 a 192.168.1.255)
    ip_range = input('C:/DEDSEC: Digite o ip')
    print(f"Iniciando escaneamento na rede {ip_range}...")
    
    # Escaneia a rede
    devices = scan(ip_range)
    
    # Gera o arquivo HTML com os dispositivos encontrados
    generate_html(devices)

if __name__ == "__main__":
    main()
