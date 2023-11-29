from os import listdir


class Parser:
    def __init__(self, rib_data_path):
        self.rib_data_path = rib_data_path

    def run(self):
        # variável para guardar os dados extraídos de todos os arquivos
        dados_por_data = dict()
        ribs = listdir(self.rib_data_path)
        ribs.remove(".gitkeep")

        # for para extrair dados de todos os arquivos na pasta de arquivos
        for rib_file_name in ribs:
            rib_file_path = self.rib_data_path + rib_file_name

            # setando/resetando variáveis de interesse
            total_anunciando_ipv4 = int()
            total_anunciando_ipv6 = int()
            total_sa = int()
            anunciando_ambos = int()
            anunciando_somente_ipv4 = int()
            anunciando_somente_ipv6 = int()
            quantidade_ipv4 = int()
            quantidade_ipv6 = int()

            # listas de sistemas autônomos
            sistemas_autonomos = dict()
            sistemas_ipv4 = set()
            sistemas_ipv6 = set()

            # listas de ips
            lista_de_ipv4 = set()
            lista_de_ipv6 = set()

            with open(rib_file_path, "r") as rib_file:
                for linha in rib_file:
                    partes = linha.strip().split('|')

                    if len(partes) >= 8:
                        # interpretando dados de uma linha """

                        ipv = partes[1].strip()
                        rota = partes[2].strip()

                        # Pega o ultimo elemento da rota
                        elementos_rota = rota.split()
                        if not elementos_rota:
                            continue
                        sistema_autonomo = elementos_rota[-1].strip()

                        # ifs para pegar as variáveis de interesse dos dados extraídos da linha """

                        # verifica se o sistema autônomo ainda não está na lista de sistemas autônomos
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

            # pegando quantidade de sistemas autônomos com ambos (ipv4 e ipv6) e com somente ipv4
            for sistema_autonomo in sistemas_ipv4:
                if sistema_autonomo in sistemas_ipv6:
                    anunciando_ambos += 1
                else:
                    anunciando_somente_ipv4 += 1

            # pegando quantidade de sistemas autônomos com somente ipv6
            for sistema_autonomo in sistemas_ipv6:
                if sistema_autonomo not in sistemas_ipv4:
                    anunciando_somente_ipv6 += 1

            dados_por_data[rib_file_name] = {
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

            break  # ler somente o primeiro arquivo

        # imprime as contagens de cada arquivo
        for chave in dados_por_data:
            print('-'*50)
            print(f"Arquivo: {chave}")
            print()
            print(f"Total de ASs: {dados_por_data[chave]['total_sa']}")
            print(f"Total de IPv4: {dados_por_data[chave]['quantidade_ipv4']}")
            print(f"Total de IPv6: {dados_por_data[chave]['quantidade_ipv6']}")
            print(f"Total ASs anunciando IPs IPv4: {dados_por_data[chave]['total_anunciando_ipv4']}")
            print(f"Total ASs anunciando IPs IPv6: {dados_por_data[chave]['total_anunciando_ipv6']}")
            print(f"ASs anunciando somente IPv4: {dados_por_data[chave]['anunciando_somente_ipv4']}")
            print(f"ASs anunciando somente IPv6: {dados_por_data[chave]['anunciando_somente_ipv6']}")
            print(f"Ambos: {dados_por_data[chave]['anunciando_ambos']}")
            print()
            counter = 0
            for sa in dados_por_data[chave]['dados_sistemas_autonomos']:
                if counter > 100:
                    break
                counter += 1
                print(
                    f'AS: {sa: >7} | '
                    f'IPv4: {dados_por_data[chave]["dados_sistemas_autonomos"][sa]["ipv4"]: >7} | '
                    f'IPv6: {dados_por_data[chave]["dados_sistemas_autonomos"][sa]["ipv6"]: >7}'
                )
            print('-'*50)
