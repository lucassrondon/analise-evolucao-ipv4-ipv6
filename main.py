contagem_ipv4 = 0
contagem_ipv6 = 0

elemento_unico = set()

with open("test.txt", "r") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split('|')
        
        if len(partes) >= 8:
            ipv = partes[1]
            rota = partes[2]
            
            # Pega o ultimo elemento da rota
            elementos_rota = rota.split()
            if elementos_rota:
                ultimo_elemento = elementos_rota[-1]
            
                # Verifica se é unico
                if ultimo_elemento not in elemento_unico:
                    elemento_unico.add(ultimo_elemento)
                    
                    # Verifica se o IP é IPv4 ou IPv6
                    if "." in ipv:
                        contagem_ipv4 += 1
                    elif ":" in ipv:
                        contagem_ipv6 += 1

# Imprime as contagens
print(f"Total de IPs IPv4: {contagem_ipv4}")
print(f"Total de IPs IPv6: {contagem_ipv6}")
