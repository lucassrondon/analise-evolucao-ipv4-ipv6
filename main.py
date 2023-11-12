import os

# variavel para guardar os dados extraidos de todos os arquivos
dados_por_data = {}

# caminho da pasta com os arquivos de dados
caminho_arquivos = "data_files/"

# for para extrair dados de todos os arquivos na pasta de arquivos
for arquivo_nome in os.listdir(caminho_arquivos):
    caminho_arquivo = caminho_arquivos + arquivo_nome

    with open(caminho_arquivo, "r") as arquivo:
        # setando/resetando variaveis de interesse
        total_anunciando_ipv4   = 0
        total_anunciando_ipv6   = 0
        total_sa                = 0
        anunciando_ambos        = 0
        anunciando_somente_ipv4 = 0
        anunciando_somente_ipv6 = 0
        quantidade_ipv4         = 0
        quantidade_ipv6         = 0

        # listas de sistemas autonomos
        sistemas_autonomos = {}
        sistemas_ipv4   = set()
        sistemas_ipv6   = set()

        # listas de ips
        lista_de_ipv4 = set()
        lista_de_ipv6 = set()

        for linha in arquivo:
            partes = linha.strip().split('|')
            
            if len(partes) >= 8:
                """ Pegando e validando dados de uma linha """

                ipv  = partes[1].strip()
                rota = partes[2].strip()
                
                # Pega o ultimo elemento da rota
                elementos_rota = rota.split()
                if not elementos_rota:
                    continue
                sistema_autonomo = elementos_rota[-1].strip()

                """ Ifs para pegar as variaveis de interesse dos dados extraidos da linha """

                # verifica se o sistema autonomo ainda não está na lista de sistemas autonomos
                if sistema_autonomo not in sistemas_autonomos:
                    sistemas_autonomos[sistema_autonomo] = {'ipv4': 0, 'ipv6': 0}
                    total_sa += 1
                
                # Pegando o total de elementos ipv4 e ipv6
                if "." in ipv and ipv not in lista_de_ipv4:
                    lista_de_ipv4.add(ipv)
                    sistemas_autonomos[sistema_autonomo]['ipv4'] += 1
                    quantidade_ipv4 += 1
                elif ":" in ipv and ipv not in lista_de_ipv6:
                    lista_de_ipv6.add(ipv)
                    sistemas_autonomos[sistema_autonomo]['ipv6'] += 1
                    quantidade_ipv6 += 1
                    
                # Verifica se o IP é IPv4 ou IPv6 e se o AS que está 
                # anunciando ainda nao está na lista
                # Importante para pegar a quantidade de elementos unicos
                if "." in ipv and sistema_autonomo not in sistemas_ipv4:
                    sistemas_ipv4.add(sistema_autonomo)
                    total_anunciando_ipv4 += 1
                elif ":" in ipv and sistema_autonomo not in sistemas_ipv6:
                    sistemas_ipv6.add(sistema_autonomo)
                    total_anunciando_ipv6 += 1

        # pegando quantidade de sistemas autonomos com ambos (ipv4 e ipv6) e com somente ipv4
        for sistema_autonomo in sistemas_ipv4:
            if sistema_autonomo in sistemas_ipv6:
                anunciando_ambos += 1
            else:
                anunciando_somente_ipv4 += 1

        # pegando quantidade de sistemas autonomos com somente ipv6
        for sistema_autonomo in sistemas_ipv6:
            if sistema_autonomo not in sistemas_ipv4:
                anunciando_somente_ipv6 += 1
        
        dados_por_data[arquivo_nome] = {
            'total_sa': total_sa,
            'quantidade_ipv4': quantidade_ipv4,
            'quantidade_ipv6': quantidade_ipv6,
            'total_anunciando_ipv4': total_anunciando_ipv4,
            'total_anunciando_ipv6': total_anunciando_ipv6,
            'anunciando_somente_ipv4': anunciando_somente_ipv4,
            'anunciando_somente_ipv6': anunciando_somente_ipv6,
            'anunciando_ambos': anunciando_ambos,
            'dados_sistemas_autonomos': sistemas_autonomos,
        }

# Imprime as contagens de cada arquivo
for chave in dados_por_data:
    print('---------------------------------------')
    print(f"Nome arquivo: {chave}")
    print(f"Total de ASes: {dados_por_data[chave]['total_sa']}")
    print(f"Total de IPv4: {dados_por_data[chave]['quantidade_ipv4']}")
    print(f"Total de IPv6: {dados_por_data[chave]['quantidade_ipv6']}")
    print(f"Total ASes anunciando IPs IPv4: {dados_por_data[chave]['total_anunciando_ipv4']}")
    print(f"Total ASes anunciando IPs IPv6: {dados_por_data[chave]['total_anunciando_ipv6']}")
    print(f"ASes anunciando somente IPv4: {dados_por_data[chave]['anunciando_somente_ipv4']}")
    print(f"ASes anunciando somente IPv6: {dados_por_data[chave]['anunciando_somente_ipv6']}")
    print(f"Ambos: {dados_por_data[chave]['anunciando_ambos']}")
    print()
    counter = 0
    for sa in dados_por_data[chave]['dados_sistemas_autonomos']:
        if counter > 100:
            break
        counter += 1
        print(f'AS: {sa}|IPv4: {dados_por_data[chave]["dados_sistemas_autonomos"][sa]["ipv4"]}|IPv6: {dados_por_data[chave]["dados_sistemas_autonomos"][sa]["ipv6"]}')
    print('---------------------------------------')