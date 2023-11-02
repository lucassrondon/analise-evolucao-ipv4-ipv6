import os

# variavel para guardar os dados extraidos de todos os arquivos
dados_por_data = {}

# caminho da pasta com os arquivos de dados
caminho_arquivos = "data_files"

# for para extrair dados de todos os arquivos na pasta de arquivos
for arquivo_nome in os.listdir(caminho_arquivos):
    caminho_arquivo = caminho_arquivos + '/' + arquivo_nome

    with open(caminho_arquivo, "r") as arquivo:
        # setando/resetando variaveis de interesse
        total_ipv4    = 0
        total_ipv6    = 0
        total_sa      = 0
        ambos         = 0
        somente_ipv4  = 0
        somente_ipv6  = 0

        # listas de sistemas autonomos
        elementos_unicos = set()
        elementos_ipv4   = set()
        elementos_ipv6   = set()

        for linha in arquivo:
            partes = linha.strip().split('|')
            
            if len(partes) >= 8:
                ipv  = partes[1].strip()
                rota = partes[2].strip()
                
                # Pega o ultimo elemento da rota
                elementos_rota = rota.split()
                if not elementos_rota:
                    continue
                ultimo_elemento = elementos_rota[-1].strip()

                # verifica se o sistema autonomo ainda não está na lista de sistemas autonomos
                if ultimo_elemento not in elementos_unicos:
                    elementos_unicos.add(ultimo_elemento)
                    total_sa += 1
                    
                # Verifica se o IP é IPv4 ou IPv6 e se ainda nao está na lista
                if "." in ipv and ultimo_elemento not in elementos_ipv4:
                    elementos_ipv4.add(ultimo_elemento)
                    total_ipv4 += 1
                elif ":" in ipv and ultimo_elemento not in elementos_ipv6:
                    elementos_ipv6.add(ultimo_elemento)
                    total_ipv6 += 1

        # pegando quantidade de sistemas autonomos com ambos (ipv4 e ipv6) e com somente ipv4
        for sistema_autonomo in elementos_ipv4:
            if sistema_autonomo in elementos_ipv6:
                ambos += 1
            else:
                somente_ipv4 += 1

        # pegando quantidade de sistemas autonomos com somente ipv6
        for sistema_autonomo in elementos_ipv6:
            if sistema_autonomo not in elementos_ipv4:
                somente_ipv6 += 1
        
        dados_por_data[arquivo_nome] = {
            'total_sa'     : total_sa,
            'total_ipv4'   : total_ipv4,
            'total_ipv6'   : total_ipv6,
            'somente_ipv4' : somente_ipv4,
            'somente_ipv6' : somente_ipv6,
            'ambos'        : ambos
        }

# Imprime as contagens de cada arquivo
for chave in dados_por_data:
    print('---------------------------------------')
    print(f"Nome arquivo: {chave}")
    print(f"Total de ASes: {dados_por_data[chave]['total_sa']}")
    print(f"Total de IPs IPv4: {dados_por_data[chave]['total_ipv4']}")
    print(f"Total de IPs IPv6: {dados_por_data[chave]['total_ipv6']}")
    print(f"Somente IPv4: {dados_por_data[chave]['somente_ipv4']}")
    print(f"Somente IPv6: {dados_por_data[chave]['somente_ipv6']}")
    print(f"Ambos: {dados_por_data[chave]['ambos']}")
    print('---------------------------------------')