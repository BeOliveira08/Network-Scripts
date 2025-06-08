from netmiko import ConnectHandler
import os
import getpass

# Configuração do dispositivo Cisco
device = {
    'device_type': 'cisco_ios',
    'host': os.getenv('CISCO_HOST', '192.168.1.1'),
    'username': os.getenv('CISCO_USER', 'admin'),
    'password': os.getenv('CISCO_PASS') or getpass.getpass('Senha do Cisco: '),
    'secret': os.getenv('CISCO_SECRET', '')  # Opcional para modo enable
}

# Comandos para criar VLANs
commands = [
    'vlan 10',
    'name TI',
    'exit',
    'vlan 20',
    'name RH',
    'exit'
]

# Conexão e execução
try:
    connection = ConnectHandler(**device)
    if device['secret']:
        connection.enable()
    output = connection.send_config_set(commands)
    print("VLANs configuradas com sucesso!\n", output)
    connection.disconnect()
except Exception as e:
    print(f"Erro: {e}")