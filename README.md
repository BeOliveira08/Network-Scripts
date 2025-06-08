# Network Scripts  
Automação de dispositivos de rede (Cisco, Fortinet) usando Python.  

## 📦 Pré-requisitos  
- Python 3.8+
- Acesso à rede dos dispositivos

Instale as dependências:
```bash
pip install -r scripts/requirements.txt
```

## 🔐 Segurança  
**Nunca coloque senhas no código!**  
Defina variáveis de ambiente ou digite quando solicitado.

## 🚀 Como usar

### Cisco VLAN
```bash
export CISCO_HOST=192.168.1.1
export CISCO_USER=admin
export CISCO_PASS=suasenha
export CISCO_SECRET=senha_privilegiada
python scripts/cisco_vlan_config.py
```
Ou apenas rode e digite a senha quando solicitado.

### Fortinet Firewall
```bash
export FGT_HOST=192.168.1.254
export FGT_USER=admin
export FGT_PASS=suasenha
python scripts/fortinet_firewall_rules.py
```
Ou apenas rode e digite a senha quando solicitado.

---

## 📄 Licença  
MIT
