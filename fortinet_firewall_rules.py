import paramiko
import os
import getpass

# Configuração do FortiGate
firewall = {
    'hostname': os.getenv('FGT_HOST', '192.168.1.254'),
    'port': int(os.getenv('FGT_PORT', 22)),
    'username': os.getenv('FGT_USER', 'admin'),
    'password': os.getenv('FGT_PASS') or getpass.getpass('Senha do FortiGate: ')
}

# Comando para criar regra de firewall
command = """
config firewall policy
    edit 0
        set name "Permit_HTTP"
        set srcintf "port1"
        set dstintf "port2"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set service "HTTP"
        set schedule "always"
    next
end
"""

# Execução via SSH
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(**firewall)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    print(stderr.read().decode())
    ssh.close()
except Exception as e:
    print(f"Erro: {e}")